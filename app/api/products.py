from fastapi import APIRouter

router = APIRouter()

@router.get("/product_by_id/{product_id}")
def get_product_by_id(product_id: str):
    return {"message": "List of products"}

@router.get("/product_by_name/{product_name}")
def get_product_by_name(product_name: str):
    return {"message": "List of products"}

@router.get("/product_all")
def list_products():
    return {"message": "List of products"}

@router.post("/add_product")
def list_products():
    return {"message": "List of products"}

@router.get("/delete_product/{product_id}")
def list_products():
    return {"message": "List of products"}