from db import get_db
from db.models import User, UserAnswer, Result, Question


# Функция для добавления пользователя в базу данных
def add_user_db(username,phone_number, level):
    with next(get_db()) as db:
        new_user = User(username=username,
                        phone_number=phone_number,
                        level=level)
        db.add(new_user)
        db.commit()
        return True



# Функция для получения всех пользователей
def get_all_users_db():
    with next(get_db()) as db:
        all_users = db.query(User).all()
        return all_users

# Функция для получения определенного пользователя по его id
def get_exact_user_db(user_id):
    with next(get_db()) as db:
        exact_user = db.query(User).filter_by(id=user_id).first()
        if exact_user:
            return  exact_user
        return False

# Функция для сохранения ответов пользователя
def user_answer_db(user_answer, user_id, q_id, level):
    with next(get_db()) as db:
        exact_question = db.query(Question).first_by(id=q_id).first()
        answers = [0, exact_question.v1, exact_question.v2, exact_question.v3, exact_question.v4]
        if exact_question:
            if exact_question.correct_answer == answers.index(user_answer):
                correctness = True
            else:
                correctness =False
            new_answer = UserAnswer(user_id=user_id,
                                    question_id=q_id,
                                    level=level,
                                    correctness=correctness,
                                    user_answer=user_answer)
            db.add(new_answer)
            db.commit()
            if correctness:
                user_result = db.query(Result).filter_by(user_id=user_id).first()
                if user_result:
                    user_result.correct_answers += 1
                    db.commit()
                    return True
                return False
        return False



# Функция для получения результата пользователя
def get_user_result_db(user_id):
    with next(get_db()) as db:
        user_result = db.query(Result).filter_by(user_id=user_id).first()
        if user_result:
            return user_result
        return False