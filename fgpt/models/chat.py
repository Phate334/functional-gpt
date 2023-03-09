from enum import Enum

from pydantic import BaseModel


class Role(str, Enum):
    system = "system"
    user = "user"
    assistant = "assistant"


class Message(BaseModel):
    role: str = Role.user
    content: str


class ChatRoom(BaseModel):
    model: str = "gpt-3.5-turbo"
    messages: list[Message]
    temperature: float = 0.7


class Choice(BaseModel):
    finish_reason: str = None
    index: int
    message: Message


class Usage(BaseModel):
    completion_tokens: int
    total_tokens: int


class Response(BaseModel):
    choices: list[Choice]
    created: int
    id: str
    model: str
    object: str
    usage: dict
