from pydantic import BaseModel

class MessageInput(BaseModel):
    message: str

class Message(MessageInput):
    id: int

class Token(BaseModel):
    token: str

class LoginUser(BaseModel):
    username: str
    password: str

class User(LoginUser):
    type: int