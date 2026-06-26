from fastapi import FastAPI
from app.api.products import router as products_router
from app.api.users import router as users_router

app = FastAPI()
app.include_router(products_router)
app.include_router(users_router, tags=["users"])

@app.get("/")
def root():
    return {"message": "API funcionando"}



