from fastapi import APIRouter
from sqlmodel import Session, select

from ..database import Message, User, engine

router = APIRouter()


@router.get("/messages", response_model=list[Message])
async def get_messages():
    with Session(engine) as session:
        messages = session.exec(select(Message)).all()
        return messages


# @router.post("/messages/add")
# async def post_message(message: MessageInput):
# message = message.message
# print(message)
# conn = connect_db()
# cur = conn.cursor()
# cur.execute("INSERT INTO messages(message) VALUES ('" + message + "')")
# conn.commit()
# conn.close()
# return [{"status": "OK"}]


@router.get("/users/type/{id}", response_model=list[User])
async def get_users_by_type(id):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.user_type == id)).all()
        return user
