from fastapi import APIRouter

router = APIRouter()

@router.get("/user_all")
def list_users():
    return {"message": "List of users"}

@router.post("/user_add")
def add_user():
    return {"message": "List of users"}

@router.get("/user_loyalty/{user_id}")
def get_user_loyalty(user_id: str):
    return {"message": "List of users"}

@router.post("/user_address/{user_id}")
def list_users():
    return {"message": "List of users"}