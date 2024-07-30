from  fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home_page() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли в качестве АДМИНИСТРАТОРА"}

@app.get("/user/{user_id}")
async def users(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def user(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
