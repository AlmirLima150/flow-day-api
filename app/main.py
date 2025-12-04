from contextlib import asynccontextmanager
from fastapi import FastAPI
from .db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="Flow Day API",
    description="API para gerenciamento pessoal modular, começando com rotina diária.",
    version="0.1.0",
    lifespan=lifespan
)

@app.get("/")
def root() -> dict:
    return {"message": "Hello World"}

@app.get("/health")
def health() -> dict:
    return {
            "status": "ok", 
            "service": "flow-day-api", 
            "version": "0.1.0"
            } 