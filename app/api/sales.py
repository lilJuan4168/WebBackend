from fastapi import APIRouter

router = APIRouter()

@router.get("/all")
def product_sales():
    return {"message": "List of sales"}