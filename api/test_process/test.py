from fastapi import APIRouter
from db.userservice import *
from db.testservice import *

test_router = APIRouter(prefix="/test", tags=["Тесты"])

@test_router.post("/add-question")
async def add_question(text: str, v1: str, v2: str, v3: str, v4: str, correctness: int, timer: int|None = None):
    new_question = add_question_db(main_question=text, v1=v1, v2=v2, v3=v3, v4=v4,
                                   correct_answer=correctness, timer=timer)
    if new_question:
        return {"status": 1, "message": "Вопрос добавлен"}
    return {"status": 0, "message": "Ошибка в добавлении вопроса"}

@test_router.get("/get-questions")
async def get_questions():
    questions = get_questions_db()
    if questions:
        return {"status": 1, "message": questions}
    return {"status": 0, "message": "Ошибка вопросы не найдены"}

@test_router.post("/add-answer")
async def add_answer(user_answer: str, user_id: int, q_id: int, level: str = "easy"):
    new_answer = user_answer_db(user_answer=user_answer, user_id=user_id, q_id=q_id, level=level)
    if new_answer:
        return {"status": 1, "message": "ответ записан"}
    return {"status": 0, "message": "Ошибка: ответ не записан"}

# Дописать получение итогово результата
@test_router.get("/get_result")
async def get_result(user_id: int):
    result_user = get_user_result_db(user_id=user_id)
    if result_user:
        return {"status": 1, "message": "Ваш результат"}
    return {"status": 0, "message": "Ошибка: неверные данные"}