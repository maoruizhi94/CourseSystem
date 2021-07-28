# 模型类

from db import db_handler


class Base:
    def save(self):
        db_handler.save(self)

    @classmethod
    def select(cls, name):
        return db_handler.select(cls, name)


class School(Base):
    def __init__(self, school_name, school_addr):
        self.name = school_name
        self.addr = school_addr
        self.course_list = []


class Course(Base):
    def __init__(self, course_name):
        self.name = course_name
        self.student_list = []


class Student(Base):
    def __init__(self, student_name, student_password):
        self.name = student_name
        self.password = student_password
        self.school = ''
        self.course = ''
        self.grade = 0

    def select_school(self, school_name):
        self.school = school_name
        self.save()

    def select_course(self, course_name, student_name):
        self.course = course_name
        self.save()
        course_obj = Course.select(course_name)
        course_obj.student_list.append(student_name)
        course_obj.save()


class Teacher(Base):
    def __init__(self, teacher_name, teacher_password):
        self.name = teacher_name
        self.password = teacher_password
        self.course = ''

    def select_course(self, course_name):
        self.course = course_name
        self.save()

    @staticmethod
    def modify_grade(student_name, grade):
        student_obj = Student.select(student_name)
        student_obj.grade = grade
        student_obj.save()


class Admin(Base):
    def __init__(self, admin_name, admin_password):
        self.name = admin_name
        self.password = admin_password

    @staticmethod
    def create_school(school_name, school_addr):
        School(school_name, school_addr).save()

    @staticmethod
    def create_course(school_obj, course_name):
        course_obj = Course(course_name)
        course_obj.save()
        school_obj.course_list.append(course_name)
        school_obj.save()

    @staticmethod
    def create_teacher(teacher_name, password):
        Teacher(teacher_name, password).save()
