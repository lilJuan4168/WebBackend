from sqlalchemy import Column, Integer, String

from app.database.base import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, foreign_key="users.id")
    product_id = Column(Integer, foreign_key="products.id")
    quantity = Column(Integer)
    total_price = Column(Integer)
    delivery_address = Column(String(200))
    