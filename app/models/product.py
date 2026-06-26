from datetime import datetime
from sqlalchemy import Column, Integer, Numeric, String, DateTime, Float, func, text
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10,2), nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    img_url: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    
