from fastapi import APIRouter
from pydantic import BaseModel
from db import connect_db

router = APIRouter()

class Message(BaseModel):
    message: str

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
async def post_message(message: Message):
    message = message.message
    print(message)
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO messages(message) VALUES ('" + message + "')")
    conn.commit()
    conn.close()
    return [{"status": "OK"}]