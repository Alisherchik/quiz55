# User
# Questions
# Result
# UserAnswers

from sqlalchemy import (Column, Integer, String, DateTime, Boolean, BigInteger, ForeignKey)
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime


# Создаем модель User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(55), nullable=False)
    phone_number = Column(String, nullable=False)
    level = Column(String, default="Select your level")
    reg_date = Column(DateTime, default=datetime.now())

# Создаем модель
class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, autoincrement=True, primary_key=True)
    main_question = Column(String, nullable=False)
    v1 = Column(String)
    v2 = Column(String)
    v3 = Column(String)
    v4 = Column(String)
    corresct_answer = Column(Integer, nullable=False)
    timer = Column(Integer, default=30)

# Создадим модель UserAnswer
class UserAnswer(Base):
    __tablename__ = "useranswers"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    user_answer = Column(String)
    timer = Column(DateTime, default=datetime.now())
    correctness = Column(Boolean, default=False)
    level = Column(String)
    user_fk = relationship(User, lazy="subquery")
    question_fk = relationship(Question, lazy="subquery")

# Создадим модель Result
class Result(Base):
    __tablename__ = "result"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    correct_answers = Column(Integer, default=0)
    level = Column(String)
    user_fk = relationship(User, lazy="subquery")