from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from ..jwt_handler import create_access_token, get_current_user

SECRET_KEY = "123"
ALGORITHM = "HS256"

router = APIRouter()


# def get_user_data(username, password):
#    conn = connect_db()
#    cur = conn.cursor()
#    cur.execute(
#        "SELECT * FROM users WHERE username = '"
#        + username
#        + "' AND password = '"
#        + password
#        + "'"
#    )
#    results = cur.fetchall()
#    conn.close()
#    if len(results) == 0:
#        return None
#    return {"username": results[0][1], "type": results[0][3]}


# @router.post("/login")
# async def login_for_access_token(user: LoginUser):
#     user_data = get_user_data(user.username, user.password)
#     if user_data is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     token = create_access_token(user_data["username"], user_data["type"])
#     return Token(token=token)


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
