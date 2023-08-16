
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property


Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(150), nullable=False)
    address = Column(String(150), nullable=False)

    @hybrid_property
    def full_name(self):
        return self.first_name + ' ' + self.last_name


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(30), unique=True, nullable=False)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(150), nullable=False)
    address = Column(String(150), nullable=False)
    group_id = Column('group_id', Integer, ForeignKey('groups.id', ondelete='CASCADE'))

    @hybrid_property
    def full_name(self):
        return self.first_name + ' ' + self.last_name


class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True)
    discipline_name = Column(String(30), unique=True, nullable=False)
    teacher_id = Column('teacher_id', Integer, ForeignKey('teachers.id', ondelete='CASCADE'))


class Score(Base):
    __tablename__ = 'score_log'
    id = Column(Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey('students.id', ondelete='CASCADE'))
    teacher_id = Column('teacher_id', Integer, ForeignKey('teachers.id', ondelete='CASCADE'))
    discipline_id = Column('discipline_id', Integer, ForeignKey('disciplines.id', ondelete='CASCADE'))
    score = Column(Integer, nullable=False)

