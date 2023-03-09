import json
import os

import openai
import typer
from dotenv import load_dotenv

from fgpt.functions import enable_funcs

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = typer.Typer()


@app.command()
def ask(
    question: str = typer.Argument(
        ...,
        help=f"Ask a question including the enable intent list: {', '.join(enable_funcs.keys())}",
    )
):
    intent_system = """Judging the intent of the input, and answers will be provided separately in JSON format for each respective intent as per requirement., without any explanation.
- if not match any intent in below,just return empty list.
===="""
    customer_service = (
        "Answer user's questions based on the following information provided.\n"
    )

    for func in enable_funcs.values():
        intent_system += func.__doc__.replace("    ", "")
    intent_res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": intent_system},
            {"role": "user", "content": question},
        ],
        temperature=0,
    )
    intents = json.loads(intent_res.choices[0]["message"]["content"])

    if not intents:
        print("can't understand your question.")
        exit(1)
    for intent in intents:
        customer_service += json.dumps(
            enable_funcs[intent["intent"]](**intent["args"]), ensure_ascii=False
        )
    intent_res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": customer_service},
            {"role": "user", "content": question},
        ],
        temperature=0.8,
    )
    print(intent_res.choices[0]["message"]["content"])


if __name__ == "__main__":
    app()
