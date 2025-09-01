import subprocess

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import init_db
from .v1.endpoints import router as v1_router
from .v2.endpoints import router as v2_router

app = FastAPI()

origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router, prefix="/api/v1", include_in_schema=False)
app.include_router(v2_router, prefix="/api/v2")

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/healthcheck")
@app.get("/healthcheck/{file}")
async def healthcheck(file = "healthcheck"):
    data = subprocess.check_output('cat %s' % file, shell=True, text=True)
    return [{"status": data}]

@app.get("/")
async def root():
    return {"message": "Move along. Nothing to see here."}
