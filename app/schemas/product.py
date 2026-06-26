# app/schemas/product.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    img_url: str
    description: str
    created_at: Optional[datetime] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    img_url: Optional[str] = None


class ProductResponse(ProductBase):
    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True