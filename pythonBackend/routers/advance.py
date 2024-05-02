from fastapi import APIRouter, WebSocket, status, Request, Depends
from fastapi.responses import RedirectResponse, HTMLResponse, StreamingResponse
from middleware.rateLimiter import limiter
from fastapi.encoders import jsonable_encoder
from typing import Annotated
from models import Item

MyRouter = APIRouter(prefix="/advance_endpoints")

@MyRouter.get("/streaming", tags=["Responses"])
def streamingVideo():
    def iterfile():
        with open("assets/TheGoat.mp4", mode="rb") as file_like:
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
    return RedirectResponse(url="https://www.youtube.com/watch?v=wSdT-SArM2Q")

@MyRouter.get("/htmlResponse", status_code=status.HTTP_423_LOCKED, tags=["Responses"])
#@limiter.limit("1/10 seconds")
async def main(request: Request):
    content = """
    <!DOCTYPE html>
<html lang="es">
<script type='text/javascript' src='https://websense.vtiger.com/load/widgets.js?id=VWT-5oCDjN6EVmVjrJDkcm74ac'></script>
<head>
    <meta charset="UTF-8">
    <title>This is a TEST</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        form {
            background-color: #f8f8f8;
            padding: 20px;
            border-radius: 8px;
        }
        label {
            display: block;
            margin-bottom: 10px;
        }
        input, button {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            box-sizing: border-box;
            border-radius: 4px;
        }
        img {
            max-width: 100px;
            height: auto;
        }
    </style>
</head>
<body>
    <h1>Person Registration</h1>
    <form>
        <label for="nombre">Name:</label>
        <input type="text" id="nombre" name="nombre" required>

        <label for="apellido">Lastname:</label>
        <input type="text" id="apellido" name="apellido" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="foto">UploadPhoto:</label>
        <input type="file" id="foto" name="foto" accept="image/*" onchange="mostrarImagen(this)">

        <img id="imagenPrevisualizacion" src="" alt="Vista previa de la imagen">

        <button type="submit">Submit Form</button>
    </form>

    <script>
        function mostrarImagen(input) {
            var file = input.files[0];
            if (file) {
                var reader = new FileReader();
                reader.onload = function(e) {
                    var imgElement = document.getElementById('imagenPrevisualizacion');
                    imgElement.src = e.target.result;
                }
                reader.readAsDataURL(file);
            }
        }
    </script>
</body>
</html>
    """    
    return HTMLResponse(content=content)

@MyRouter.get("/rateLimit", tags=["Responses"], summary="request rete limit", description="this limit the amount of request you can do.")
@limiter.limit("1/5 seconds")
def hello(request: Request, username: str):
    return f"rate limit test {username}..."

@MyRouter.put("/items/{id}", tags=["Responses"])
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    return json_compatible_item_data

