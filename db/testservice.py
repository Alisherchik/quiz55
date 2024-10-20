from db import get_db
from db.models import Question, Result


# Функция для добавления вопроса
def add_question_db(main_question, v1, v2, v3, v4,
                    correct_answer, timer=None):
    with next(get_db()) as db:
        new_question = Question(main_question=main_question,
                                v1=v1, v2=v2, v3=v3, v4=v4,
                                correct_answer=correct_answer, timer=timer)
        db.add(new_question)
        db.commit()
        return True

# Функция для получения первых двадцати вопросов
def get_questions_db():
    with next(get_db()) as db:
        all_question = db.query(Question).all() #Question(), )
        return all_question[:20]


# Функция для получения топ 10
def get_10_leaders_db():
    with next(get_db()) as db:
        leaders = db.query(Result.user_id).order_by(Result.correct_answers.desc())
        return leaders[:10]



# Добавление информации в базу данных
# new_object = Table(name=name)
# db.add(new_object)
# db.add(Table(name=name)
# db.commit()

# Получение всех данных
# all_objects = db.query(Table).all()

# Фильтрация данных
# db.query(Table.filter_by(name=name).first() // .all()