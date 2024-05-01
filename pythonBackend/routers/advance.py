from fastapi import APIRouter, WebSocket, status, Request, Depends
from fastapi.responses import RedirectResponse, HTMLResponse, StreamingResponse
from middleware.rateLimiter import limiter
from fastapi.encoders import jsonable_encoder
from typing import Annotated
from dependencies import get_current_username
from models import Item

MyRouter = APIRouter(prefix="/advance_params")

@MyRouter.get("/streaming", tags=["Responses"])
def main():
    def iterfile():
        with open("assets/mediapipe.mp4", mode="rb") as file_like:
            yield from file_like
    return StreamingResponse(iterfile(), media_type="video/mp4")

@MyRouter.get("/chatWS", tags=["Responses"])
async def get():
    html = """<!DOCTYPE html>
    <html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
    </html>"""
    return HTMLResponse(html)

@MyRouter.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

@MyRouter.get("/redirect", tags=['Responses'])
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@MyRouter.get("/htmlResponse", status_code=status.HTTP_423_LOCKED, tags=["Responses"])
#@limiter.limit("1/10 seconds")
async def main(request: Request):
    content = """
    <head>
    Testing HTML
    </head>
    <body>
    <form action="/files/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    <script type='text/javascript' src='https://websense.vtiger.com/load/widgets.js?id=VWT-5oCDjN6EVmVjrJDkcm74ac'></script>
    </body>"""    
    return HTMLResponse(content=content)

@MyRouter.get("/rateLimit", tags=["Responses"], summary="request rete limit", description="this limit the amount of request you can do.")
@limiter.limit("1/5 seconds")
def hello(request: Request, username: Annotated[str, Depends(get_current_username)]):
    return f"rate limit test {username}"

@MyRouter.put("/items/{id}", tags=["Responses"])
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    return json_compatible_item_data

@MyRouter.get("/htmlResponse/vtiger", status_code=status.HTTP_423_LOCKED, tags=["Responses"])
#@limiter.limit("1/10 seconds")
async def vtiger(request: Request):
    content = """

    <script type='text/javascript' src='https://websense.vtiger.com/load/widgets.js?id=VWT-5oCDjN6EVmVjrJDkcm74ac'></script>
    """   
    return HTMLResponse(content=content)