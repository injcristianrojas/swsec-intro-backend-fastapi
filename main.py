import subprocess
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from db import init_db

from v1.endpoints import router as v1_router
from v2.endpoints import router as v2_router

init_db()

app = FastAPI()

app.include_router(v1_router, prefix="/api/v1", include_in_schema=False)
app.include_router(v2_router, prefix="/api/v2")

print(app.routes)

@app.get("/healthcheck")
@app.get("/healthcheck/{file}")
async def healthcheck(file = "healthcheck"):
    data = subprocess.check_output('cat %s' % file, shell=True, text=True)
    return [{"status": data}]

@app.get("/")
async def root():
    return {"message": "Move along. Nothing to see here."}
