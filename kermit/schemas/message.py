from pydantic import BaseModel, Field


class Message(BaseModel):

    id: str = Field
    content: str = Field
