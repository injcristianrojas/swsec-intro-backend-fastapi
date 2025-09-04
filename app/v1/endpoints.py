from fastapi import APIRouter
from sqlmodel import Session, select

from ..database import Message, MessageInsert, User, engine

router = APIRouter()


@router.get("/messages", response_model=list[Message])
async def get_messages():
    with Session(engine) as session:
        messages = session.exec(select(Message)).all()
        return messages


@router.post("/messages/add")
async def post_message(message_insert: MessageInsert):
    with Session(engine) as session:
        session.add(Message(message=message_insert.message))
        session.commit()
    return [{"status": "OK"}]


@router.get("/users/type/{id}", response_model=list[User])
async def get_users_by_type(id):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.user_type == id)).all()
        return user
