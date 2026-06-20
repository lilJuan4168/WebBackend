from fastapi import APIRouter

router = APIRouter()

@router.get("/all")
def list_users():
    return {"message": "List of users"}