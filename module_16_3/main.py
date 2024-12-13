from fastapi import FastAPI, Path
from typing import Annotated

from pyexpat.errors import messages

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'} # наша импровизированная база данных

@app.get('/users') # на данный запрос нам ...
async def get_users() -> dict:
    return users # возвращается наша база данных



@app.post('/user/{username}/{age}') # запрос регистрация пользователя
async def create_user(username: Annotated[str, Path(min_length=3, max_length=15, description='Введите Ваше имя', example=' Сергей')]
                      , age: int) -> str:
    current_index = str(int(max(users, key=int)) + 1) # текущий индекс = (находим номер последней строки БД и прибавляем один
    users[current_index] = username, age # добавляем в базу данные
    return f'Пользователь {current_index} зарегистрирован!'

@app.put('/user/{user_id}/{username}/{age}') # запрос на изменение данных пользователя
async def update_user(user_id: str = Path(ge=1, le=100, description='Введите возраст', example= '1')
                      , username: str =Path(min_length=3, max_length=20, description=' Введите Ваше имя', example= 'Сергей')
                      , age: int = 30) -> str:
    users[user_id] = user_id, username, age
    return f'Информация о пользователе id# {user_id} обновлена'

@app.delete('/user/{user_id}') # запрос на удаление конкретного пользователя
async def delite_user(user_id: str) -> str:
    users.pop(user_id)
    return f'Пользователь {user_id} удалён'
