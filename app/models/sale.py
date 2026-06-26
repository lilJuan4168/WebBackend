from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, Float, func, text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Sale(Base):
    __tablename__ = "sale"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("product.id"))
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    unit_price: Mapped[float] = mapped_column(Numeric(10,2), nullable=False)
    total_price: Mapped[float] = mapped_column(Numeric(10,2), nullable=False)
    delivery_address: Mapped[str] = mapped_column(String(200), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    