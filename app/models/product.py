import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from app.database.base import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(100), unique=True)
    price = Column(Float)
    stock = Column(Integer)
    img_url = Column(String(200))
    description = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)
    
