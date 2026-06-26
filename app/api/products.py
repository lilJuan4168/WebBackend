from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
)
from app.services.product_service import (
    get_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product,
)

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/all", response_model=list[ProductResponse])
def read_products(db: Session = Depends(get_db)):
    return get_products(db)


@router.get("/by-id/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return product


@router.post("/create", response_model=ProductResponse)
def create_new_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
):
    return create_product(db, product)


@router.put("/update/{product_id}", response_model=ProductResponse)
def update_existing_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db),
):
    updated = update_product(db, product_id, product)

    if not updated:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return updated


@router.delete("/delete/{product_id}")
def delete_existing_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_product(db, product_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return {"message": "Producto eliminado correctamente"}