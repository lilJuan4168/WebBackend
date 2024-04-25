from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from datetime import datetime

class Position(str, Enum):
    engineer = "Engineer"
    doctor = "Doctor"
    mechanic = "Mechanic"
    helper = "Helper"
    nurse = "Nurse"
    programmer = "Programmer"

class User(BaseModel):
    name: str
    age: int = Field(ge=18, le=30)
    fiends: list[str] = Field(default=None, max_items=3)
    email: EmailStr = Field(default=None)

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None