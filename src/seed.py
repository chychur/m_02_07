from random import randint

from faker import Faker

from db import session
from models import Teacher, Student, Discipline, Group, Score


fake = Faker('en_US')

ONE = 1

NUMBER_TEACHERS = 5+ONE

name_groups = ['PY-1', 'MTH-13', 'COR-24']
NUMBER_GROUPS = 3

NUMBER_STUDENTS = 30+ONE

name_disciplines = ['Physics', 'Math', 'Cybernetics', 'Hydraulics', 'Philosophy']
NUMBER_DISCIPLINES = 5

NUMBER_SCORES = 20
VALUE_SCORES = 10


def create_teachers():
    for _ in range(ONE, NUMBER_TEACHERS):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            phone=fake.phone_number(),
            address=fake.address()
        )
        session.add(teacher)
    session.commit()


def create_group(groups):
    for group_name in groups:
        group = Group(
            group_name=group_name
        )
        session.add(group)
    session.commit()


def create_students():
    for _ in range(ONE, NUMBER_STUDENTS):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            phone=fake.phone_number(),
            address=fake.address(),
            group_id=randint(ONE, NUMBER_GROUPS)
        )
        session.add(student)
    session.commit()


def create_discipline(disciplines):
    id_ = ONE
    for discipline_name in disciplines:
        discipline = Discipline(
            discipline_name=discipline_name,
            teacher_id=id_
        )
        id_ += ONE
        session.add(discipline)
    session.commit()


def create_score_log():
    score_log = []
    for student in range(ONE, NUMBER_STUDENTS):
        for teacher in range(ONE, NUMBER_TEACHERS):
            for score in range(NUMBER_SCORES):
                r_score = randint(ONE, VALUE_SCORES)
                result = (student, teacher, teacher, r_score)
                score_log.append(result)

    for item in score_log:
        score = Score(
            student_id=item[0],
            teacher_id=item[1],
            discipline_id=item[2],
            score=item[3]
        )
        # print(score.student_id, score.teacher_id, score.discipline_id, score.score, '\n')
        session.add(score)
    session.commit()


if __name__ == '__main__':
    create_teachers()
    create_group(name_groups)
    create_students()
    create_discipline(name_disciplines)
    create_score_log()

