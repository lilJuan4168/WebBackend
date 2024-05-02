from fastapi import APIRouter, Body, Path, Query, Form, UploadFile, Depends
from models import Position, User
from typing import Annotated
from routers.security import get_current_user

MyRouter_params = APIRouter(prefix="/params")

@MyRouter_params.post("/enum", tags=["RequestType"], description="You can choose your job.")
def job_position(position: Annotated[Position, Depends(get_current_user)]):
    return f"your position is {position.value}..."

@MyRouter_params.post("/basemodelPlusBody", tags=["RequestType"], description="You can share some information of yourself.")
def registration(user: User, availability: Annotated[bool, Body(description="this is the availability")]):
    return user, availability

@MyRouter_params.post("/path/{job}", tags=["RequestType"], description="Write a job no more than 8 letters.")
def job(job: Annotated[str, Path(max_length=8)]):
    return job

@MyRouter_params.post("/query", tags=["RequestType"], description="Write your address.")
def address(my_address: str, user: Annotated[str, Depends(get_current_user)]):
    return my_address, user

@MyRouter_params.post("/body", tags=["RequestType"], description="Write your name and hobby.")
def body_param(name: Annotated[str, Body(max_length=10)], hobby: Annotated[str, Body(max_length=12)]):
    return {"name": name, "hobby": hobby}

@MyRouter_params.post("/forms", tags=["RequestType"], description="Write your username and password by form.")
def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return username, password

@MyRouter_params.post("/files", tags=["RequestType"], description="Upload any file you want.")
async def create_file(file: UploadFile):
    content = file.read()
    return {f"file_size: {file.filename}, {file.content_type}", content}