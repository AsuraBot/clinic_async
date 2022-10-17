from pydantic import BaseModel
from datetime import date
from typing import Optional


class SpecialistSchema(BaseModel):
    """Схема специалиста."""

    name: str
    photo: Optional[str]
    start_work_date: date
    description: str

    class Config:
        orm_mode = True
