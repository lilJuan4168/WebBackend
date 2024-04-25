from fastapi import APIRouter, Body, Path, Query, Form, UploadFile
from models import Position, User
from typing import Annotated

MyRouter_params = APIRouter(prefix="/params")

@MyRouter_params.post("/enum", tags=["RequestType"])
def job_position(position: Position):
    return f"your position is {position.value}..."

@MyRouter_params.post("/basemodelPlusBody", tags=["RequestType"])
def registration(user: User, availability: Annotated[bool, Body(description="this is the availability")]):
    return user, availability

@MyRouter_params.post("/path/{job}", tags=["RequestType"])
def job(job: Annotated[str, Path(max_length=5)]):
    return job

@MyRouter_params.post("/query", tags=["RequestType"])
def address(my_address: Annotated[str, Query(max_length=5)]):
    return my_address

@MyRouter_params.post("/body", tags=["RequestType"])
def body_param(name: Annotated[str, Body(max_length=10)], hobby: Annotated[str, Body(max_length=12)]):
    return {"name": name, "hobby": hobby}

@MyRouter_params.post("/forms", tags=["RequestType"])
def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return username, password

@MyRouter_params.post("/files", tags=["RequestType"])
async def create_file(file: UploadFile):
    content = file.read()
    return {f"file_size: {file.filename}, {file.content_type}", content}