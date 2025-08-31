from fastapi import APIRouter
from ..models import MessageInput
from ..db import connect_db

router = APIRouter()

@router.get("/messages")
async def get_messages():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM messages")
    results = cur.fetchall()
    conn.close()
    json_results = []
    for row in results:
        json_results.append({"id": row[0], "message": row[1]})
    return json_results

@router.post("/messages/add")
async def post_message(message: MessageInput):
    message = message.message
    print(message)
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO messages(message) VALUES ('" + message + "')")
    conn.commit()
    conn.close()
    return [{"status": "OK"}]

@router.get("/users/type/{id}")
async def get_users_by_type(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE user_type = " + id)
    results = cur.fetchall()
    conn.close()
    json_results = []
    for row in results:
        json_results.append({"id": row[0], "username": row[1], "password": row[2]})
    return json_results
