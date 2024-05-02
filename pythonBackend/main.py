from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from middleware.analytics import *
from middleware.rateLimiter import rate_limit_exceeded_handler_status_code, limiter, RateLimitExceeded
from routers.advance import MyRouter
from routers.params import MyRouter_params
from routers.security import My_Security
from api_analytics.fastapi import Analytics
from models import *
import uvicorn

# FastAPI instnce
app = FastAPI(title="PythonBackend", description="This is a practice backend to show the power of fastapi.", version="1.0")

# Include routers
app.include_router(MyRouter)
app.include_router(MyRouter_params)
app.include_router(My_Security)

# Create analytics
app.add_middleware(Analytics, api_key="6b5f90f0-b010-4eea-8fa5-3e4795e5b813") 

# Configure error handler
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler_status_code)

# Add static files
app.mount("/static", StaticFiles(directory="assets"), name="static")


@app.get("/")
def welcome():
    content = """
    <!DOCTYPE html>
    <html lang="es">
    <body>
    <meta charset="UTF-8">
    <title>Welcome</title>
    <h1>Hello Everyone!!<h1>
    <style>
        h1 {
            font-family: Arial, sans-serif;
            background-color: #f8f8f8;
        }  
    </style>
    </body>    
    </html>
    """
    return HTMLResponse(content=content)


if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=8000, host="0.0.0.0",log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()


