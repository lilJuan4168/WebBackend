from sqlalchemy import Column, Integer, String, Float

from app.database.base import Base


class Sale(Base):
    __tablename__ = "sale"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, foreign_key="user.id")
    product_id = Column(Integer, foreign_key="product.id")
    quantity = Column(Integer)
    unit_price = Column(Float)
    total_price = Column(Float)
    delivery_address = Column(String(200))
    