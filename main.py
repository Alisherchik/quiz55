from fastapi import FastAPI
from api.user_api.user import user_router
from api.test_process.test import test_router
app = FastAPI(docs_url="/swagger")
from db import Base, engine
# создаем базу данных и делаем все миграции
Base.metadata.create_all(bind=engine)
# Регистрация компонентов проекта (роутеров)
app.include_router(user_router)
app.include_router(test_router)