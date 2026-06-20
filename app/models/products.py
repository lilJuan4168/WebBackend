from sqlalchemy import Column, Integer, String

from app.database.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    price = Column(Integer)
    stock = Column(Integer)
    img_url = Column(String(200))
    description = Column(String(500))
    
