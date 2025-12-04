from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str | None = None
    priority: str = Field(default="medium")
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    is_done: bool = Field(default=False)