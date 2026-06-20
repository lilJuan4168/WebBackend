from fastapi import APIRouter

router = APIRouter()

@router.get("/all")
def list_products():
    return {"message": "List of products"}



