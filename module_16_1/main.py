from fastapi import FastAPI, Query
app = FastAPI()
@app.get("/")
async def Get_main_page():
    return "Главная страница"
@app.get("/user/admin")
async def Get_admin_admin():
    return "Вы вошли как администратор"
@app.get("/user/{user_id}")
async def Get_user_Number(user_id: int):
    return {f"Вы вошли как пользователь № {user_id}"}
@app.get("/user")
async def Get_user_info(username: str = Query(...), age: int = Query(...)):
    return {f"Информация о пользователе. Имя: '{username}', Возраст: {age}."}