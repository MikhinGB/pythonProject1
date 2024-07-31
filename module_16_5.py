from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int = None

@app.get("/")
def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get(path="/user/{user_id}")
def get_users(request: Request, user_id: int) -> HTMLResponse:
    user_id = user_id - 1
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.post("/")
def post_user(request: Request, user: User, username, age) -> HTMLResponse:
    user.id = len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return templates.TemplateResponse("users.html", {"request": request, "user_id": user.id, "username": username, "age": age})


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username, age) -> str:
    try:
        edit_user = users[(user_id - 1)]
        edit_user.username = username
        edit_user.age = age
        return f"User named {username} {age} years old with ID={user_id} updated!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id-1)
        return f"User ID={user_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

