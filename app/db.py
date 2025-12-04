from sqlmodel import SQLModel, create_engine 
import os
from .models import Task

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable not set")

engine = create_engine(DATABASE_URL, echo=True)

def init_db() -> None:
    SQLModel.metadata.create_all(engine)