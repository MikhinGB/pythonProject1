from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int = None

@app.get("/users")
def get_all_users() -> List[User]:
    return users

#
# @app.get(path="/user/{username}/{age}")
# def get_message(user_id: int) -> User:
#     try:
#         return users[user_id]
#     except IndexError:
#         raise HTTPException(status_code=404, detail="User not found")


@app.post("/user/{username}/{age}")
async def added_user(user: User, username, age) -> str:
    user.id = len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return f'User named {user.username} {user.age} years old with ID={user.id} added'


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
