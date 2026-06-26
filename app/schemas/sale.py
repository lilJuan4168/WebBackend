# app/schemas/sale.py

from pydantic import BaseModel
from datetime import datetime


class SaleBase(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    unit_price: float
    total_price: float
    delivery_address: str
    created_at: datetime


class SaleCreate(SaleBase):
    pass


class SaleResponse(SaleBase):
    user_id: int
    product_id: int
    created_at: datetime

    class Config:
        from_attributes = True

