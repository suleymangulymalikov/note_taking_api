from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NoteCreate(BaseModel):
    title: str
    content: str
    tags: Optional[list[str]] = None


class Note(NoteCreate):
    id: int
    created_at: datetime
    updated_at: datetime