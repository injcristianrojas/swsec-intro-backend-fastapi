from fastapi import FastAPI
from db import init_db

from v1.endpoints import router as v1_router

init_db()

app = FastAPI()

app.include_router(v1_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Move along. Nothing to see here."}
