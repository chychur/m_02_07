from sqlalchemy import func, and_
from db import session
from models import Teacher, Student, Discipline, Group, Score


# Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def select_1():
    result = (
        session.query(Student.full_name, func.round(func.avg(Score.score), 2).label('avg_score'))
        .join(Score, Score.student_id == Student.id)
        .group_by(Student.id)
        .order_by(func.avg(Score.score).desc())
        .limit(5)
        .all()
    )
    return result


# Знайти студента із найвищим середнім балом з певного предмета.
def select_2(name_discipline):
    result = (
        session.query(Student.full_name, func.round(func.avg(Score.score), 2).label('avg_score'))
        .join(Score, Score.student_id == Student.id)
        .join(Discipline, Discipline.id == Score.discipline_id)
        .filter(Discipline.discipline_name == name_discipline)
        .group_by(Student.id)
        .order_by(func.avg(Score.score).desc())
        .first()
    )
    return result


# Знайти середній бал у групах з певного предмета.
def select_3(name_discipline):
    result = (
        session.query(Group.group_name, func.round(func.avg(Score.score), 2).label('avg_score'))
        .join(Student, Student.group_id == Group.id)
        .join(Score, Score.student_id == Student.id)
        .join(Discipline, Discipline.id == Score.discipline_id)
        .filter(Discipline.discipline_name == name_discipline)
        .group_by(Group.id)
        .all()
    )
    return result


# Знайти середній бал на потоці (по всій таблиці оцінок).
def select_4():
    result = (
        session.query(func.round(func.avg(Score.score), 2).label('avg_score')).scalar()
    )
    return result


# Знайти, які курси читає певний викладач.
def select_5(teacher):
    result = (
        session.query(Discipline.discipline_name)
        .join(Teacher, Teacher.id == Discipline.teacher_id)
        .filter(Teacher.full_name == teacher)
        .all()
    )
    return result


# Знайти список студентів у певній групі.
def select_6(group_name):
    result = (
        session.query(Student.full_name, Student.email, Student.phone, Student.address, Group.group_name)
        .join(Group, Group.id == Student.group_id)
        .filter(Group.group_name == group_name)
        .all()
    )
    return result


# Знайти оцінки студентів в окремій групі з певного предмета.
def select_7(group_name, name_discipline):
    result = (
        session.query(Student.full_name, Group.group_name, Score.score)
        .join(Group, Group.id == Student.group_id)
        .join(Score, Score.student_id == Student.id)
        .join(Discipline, Discipline.id == Score.discipline_id)
        .filter(Group.group_name == group_name, Discipline.discipline_name == name_discipline)
        .all()
    )
    return result


#Знайти середній бал, який ставить певний викладач зі своїх предметів.
def select_8(teacher):
    result = (
        session.query(func.round(func.avg(Score.score), 2).label('avg_score'))
        .join(Teacher, Teacher.id == Score.teacher_id)
        .filter(Teacher.full_name == teacher)
        .scalar()
    )
    return result



#Знайти список курсів, які відвідує певний студент.
def select_9(student):
    result = (
        session.query(Discipline.discipline_name)
        .join(Score, Score.discipline_id == Discipline.id)
        .join(Student, Student.id == Score.student_id)
        .filter(Student.full_name == student)
        .group_by(Discipline.id)
        .all()
    )
    return result


# Список курсів, які певному студенту читає певний викладач.
def select_10(student, teacher):
    result = (
        session.query(Discipline.discipline_name)
        .join(Score, Score.discipline_id == Discipline.id)
        .join(Teacher, Teacher.id == Score.teacher_id)
        .join(Student, Student.id == Score.student_id)
        .filter(Student.full_name == student, Teacher.full_name == teacher)
        .group_by(Discipline.id)
        .all()
    )
    return result



if __name__ == '__main__':
    # s1 = select_1()
    # print(s1)
    # s2 = select_2('Math')
    # print(s2)
    # s3 = select_3('Math')
    # print(s3)
    # s4 = select_4()
    # print(s4)
    # s5 = select_5('Diana Wright')
    # print(s5)
    # s6 = select_6('MTH-13')
    # print(s6)
    # s7 = select_7('MTH-13', 'Math')
    # print(s7)
    # s8 = select_8('Diana Wright')
    # print(s8)
    # s9 = select_9('Rachel Robles')
    # print(s9)
    s10 = select_10('Rachel Robles', 'Diana Wright')
    print(s10)
