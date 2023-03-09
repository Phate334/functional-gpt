import json
import os

import openai
import typer
from dotenv import load_dotenv

from fgpt.functions import enable_funcs

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = typer.Typer()
intent = """Judging the intent of the input and returning the answer only in JSON format according to the respective requirements, without any explanation.
- when no intent is met
[{"intent": "none"}]
===="""

for func in enable_funcs.values():
    intent += func.__doc__.replace("    ", "")


@app.command()
def ask(question: str = typer.Argument(..., help="The question to ask")):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": intent},
            {"role": "user", "content": question},
        ],
    )
    print(res)


if __name__ == "__main__":
    app()
