from pydantic import BaseModel

class MessageInput(BaseModel):
    message: str

class Message(MessageInput):
    id: int

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginUser(BaseModel):
    username: str
    password: str

class User(LoginUser):
    type: int