# app/schemas/user.py

from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    id: int
    username: str
    full_name: str
    phone_number: str
    email: EmailStr
    address: str
    delivery_address: str
    royalty_points: int
    created_at: datetime


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True


