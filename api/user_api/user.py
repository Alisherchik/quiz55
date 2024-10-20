from fastapi import APIRouter
from db.userservice import *
from db.testservice import get_10_leaders_db

user_router = APIRouter(prefix="/user", tags=["Пользовательская часть"])

# регистрация юзеры
@user_router.post("/register")
async def register_user(username: str, phone_number: str, level: str = "easy"):

    result = add_user_db(username=username, phone_number=phone_number, level=level)
    if result:
        return {"status": 1, "message": "вы удачно зерегистрировались"}
    return {"status": 0, "message": "ошибка регистрации"}


# получение всех пользователей
@user_router.get("/get-users")
async def get_users():
    all_users = get_all_users_db()
    if all_users:
        return {"status": 1, "message": all_users}
    return {"status": 0, "message": "юзеры не найдены"}

@user_router.get("/get-user")
async def get_user(user_id: int):
    user_info = get_exact_user_db(user_id=user_id)
    if user_info:
        return {"status": 1, "message": user_info}
    return {"status": 0, "message": "юзер не найден"}

@user_router.get("/top10")
async def get_top_10():
    top_10 = get_10_leaders_db()
    if top_10:
        return {"status": 1, "message": top_10}
    return {"status": 0, }