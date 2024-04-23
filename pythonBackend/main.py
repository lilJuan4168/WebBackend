from fastapi import FastAPI, Query, Form, Body, Request, File, UploadFile, HTTPException, status, Path, Depends
import uvicorn
from fastapi.responses import RedirectResponse, HTMLResponse

from datetime import datetime
from fastapi.staticfiles import StaticFiles

from fastapi.encoders import jsonable_encoder

from api_analytics.fastapi import Analytics


app = FastAPI()

security = HTTPBasic()

# add static files
app.mount("/static", StaticFiles(directory="assets"), name="static")

# Crear analitica
app.add_middleware(Analytics, api_key="6b5f90f0-b010-4eea-8fa5-3e4795e5b813")  


@app.get("/testing", tags=['responses'])
#@limiter.limit("1/5 seconds")
def testing(request: Request):
    """
    # Testing descriptions
    This is a test for markdown descriptions in fastapi.
    - title
    - paragraph
    - images
    **This is bold**
    ![mi image](/static/logo.jpg)

    """
    return f"rate limit test"

@app.get("/rateLimit", tags=['responses'], summary="request rete limit", description="this limit the amount of request you can do.")
#@limiter.limit("1/5 seconds")
def hello(request: Request, username: Annotated[str, Depends(get_current_username)]):
    return f"rate limit test {username}"

@app.post("/enum")
def job_position(position: Position):
    return f"your position is {position.value}..."

@app.post("/basemodelPlusBody", tags=["requestType"])
def registration(user: User, availability: Annotated[str, Body(description="this is the availability")]):
    return user, availability

@app.post("/path/{job}", tags=["requestType"])
def job(job: Annotated[str, Path(max_length=5)]):
    return job

@app.post("/query", tags=["requestType"])
def address(my_address: Annotated[str, Query(max_length=5)]):
    return my_address

@app.post("/forms", tags=["requestType"])
def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return username, password

@app.get("/teleport", tags=['responses'])
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@app.post("/files", tags=["requestType"])
async def create_file(file: UploadFile):
    content = file.read()
    return {f"file_size: {file.filename}, {file.content_type}", content}

@app.get("/htmlResponse", status_code=status.HTTP_423_LOCKED, tags=["responses"])
#@limiter.limit("1/10 seconds")
async def main(request: Request):
    content = """
    <body>
    <form action="/files/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    </body>"""    
    return HTMLResponse(content=content)

@app.put("/items/{id}", tags=['encoder'])
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    return json_compatible_item_data

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=8000, host="0.0.0.0",log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()


