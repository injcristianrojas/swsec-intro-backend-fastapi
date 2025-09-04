from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select, text

from ..database import Message, MessageInsert, User, UserLogin, Token, engine
from ..jwt_handler import create_access_token, get_current_user

SECRET_KEY = "123"
ALGORITHM = "HS256"

router = APIRouter()


@router.post("/login")
async def login_for_access_token(user_login: UserLogin):
    with Session(engine) as session:
        user = session.exec(text(f"SELECT * FROM user WHERE username = '{user_login.username}' AND password = '{user_login.password}'")).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        token = create_access_token(user.username, user.user_type)
        return Token(token=token)


@router.get("/messages", response_model=list[Message])
async def get_messages(current_user: Annotated[User, Depends(get_current_user)]):
    with Session(engine) as session:
        messages = session.exec(select(Message)).all()
        return messages


@router.post("/messages/add")
async def post_message(
    message_insert: MessageInsert,
    current_user: Annotated[User, Depends(get_current_user)],
):
    with Session(engine) as session:
        session.add(Message(message=message_insert.message))
        session.commit()
    return [{"status": "OK"}]


@router.get("/users/type/{id}", response_model=list[User])
async def get_users_by_type(
    id, current_user: Annotated[User, Depends(get_current_user)]
):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.user_type == id)).all()
        return user
