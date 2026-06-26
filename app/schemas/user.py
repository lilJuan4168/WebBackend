# app/schemas/user.py

from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: EmailStr
    address: str
    royalty_points: int


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True


