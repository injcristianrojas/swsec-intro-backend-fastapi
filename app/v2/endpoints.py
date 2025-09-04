from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from ..database import User, UserLogin, Token, engine
from ..jwt_handler import create_access_token, get_current_user

SECRET_KEY = "123"
ALGORITHM = "HS256"

router = APIRouter()


@router.post("/login")
async def login_for_access_token(user_login: UserLogin):
    with Session(engine) as session:
        user = session.exec(
            select(User)
            .where(User.username == user_login.username)
            .where(User.password == user_login.password)
        ).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        token = create_access_token(user.username, user.user_type)
        return Token(token=token)


# @router.get("/messages")
# async def get_messages(current_user: Annotated[User, Depends(get_current_user)]):
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM messages")
#     results = cur.fetchall()
#     conn.close()
#     json_results = []
#     for row in results:
#         json_results.append(Message(id=row[0], message=row[1]))
#     return json_results


# @router.post("/messages/add")
# async def post_message(message: MessageInput, current_user: Annotated[User, Depends(get_current_user)]):
#     message = message.message
#     print(message)
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute("INSERT INTO messages(message) VALUES ('" + message + "')")
#     conn.commit()
#     conn.close()
#     return [{"status": "OK"}]


# @router.get("/users/type/{id}")
# async def get_users_by_type(id, current_user: Annotated[User, Depends(get_current_user)]):
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM users WHERE user_type = " + id)
#     results = cur.fetchall()
#     conn.close()
#     json_results = []
#     for row in results:
#         json_results.append({"id": row[0], "username": row[1]})
#     return json_results
