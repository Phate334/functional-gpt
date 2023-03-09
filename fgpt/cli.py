import json
import os

import openai
import typer
from dotenv import load_dotenv

from fgpt.functions import enable_funcs
from fgpt.models.chat import ChatRoom, Message, Response

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
- when no intent is met
[{"intent": "none"}]
===="""
    customer_service = (
        "Answer user's questions based on the following information provided.\n"
    )

    for func in enable_funcs.values():
        intent_system += func.__doc__.replace("    ", "")
    chatroom = ChatRoom(
        messages=[
            Message(role="system", content=intent_system),
            Message(role="user", content=question),
        ],
        temperature=0,
    )
    intent_response = Response.parse_obj(
        openai.ChatCompletion.create(**chatroom.dict())
    )
    intents = json.loads(intent_response.choices[0].message.content)
    if not intents:
        print("can't understand your question.")
        exit(1)
    for intent_obj in intents:
        customer_service += json.dumps(
            enable_funcs[intent_obj["intent"]](**intent_obj["args"]), ensure_ascii=False
        )
    response_room = ChatRoom(
        messages=[
            Message(role="system", content=customer_service),
            Message(role="user", content=question),
        ],
        temperature=0.8,
    )
    answer_response = Response.parse_obj(
        openai.ChatCompletion.create(**response_room.dict())
    )
    print(answer_response.choices[0].message.content)


if __name__ == "__main__":
    app()
