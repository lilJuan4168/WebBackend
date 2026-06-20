from fastapi import FastAPI
from app.api.products import router as products_router
from app.api.users import router as users_router
from uvicorn import run

app = FastAPI()
app.include_router(products_router, prefix="/products", tags=["products"])
app.include_router(users_router, prefix="/users", tags=["users"])

@app.get("/")
def root():
    return {"message": "API funcionando"}


if __name__ == "__main__":
    run("app.main:app", host="127.0.0.1", port=8000, reload=True)

