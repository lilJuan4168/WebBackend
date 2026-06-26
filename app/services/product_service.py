# app/services/product_service.py

from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def get_products(db: Session):
    return db.query(Product).all()


def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def create_product(db: Session, product_data: ProductCreate):
    new_product = Product(**product_data.model_dump())

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


def update_product(db: Session, product_id: int, product_data: ProductUpdate):
    product = get_product_by_id(db, product_id)

    if not product:
        return None

    for key, value in product_data.model_dump(exclude_unset=True).items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product


def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)

    if not product:
        return None

    db.delete(product)
    db.commit()

    return product