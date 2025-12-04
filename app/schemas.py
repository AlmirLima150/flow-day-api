from datetime import datetime
from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = None  
    priority: str = Field(default="medium")
   
class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None
    priority: str
    created_at: datetime
    is_done: bool

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: str | None = None
    is_done: bool | None = None