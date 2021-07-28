from lib import common
from db import models

teacher_logger = common.customize_logger('teacher')


def login_interface(teacher_name, teacher_pwd):
    # 1.判断讲师对象是否存在
    teacher_obj = models.Teacher.select(teacher_name)
    if not teacher_obj:
        msg = '讲师「{}」不存在，请联系管理员！'.format(teacher_name)
        teacher_logger.debug(msg)
        return True, msg
    # 2.判断密码是否正确
    if teacher_obj.password == teacher_pwd:
        msg = '讲师「{}」登录成功'.format(teacher_name)
        teacher_logger.debug(msg)
        return True, msg
    else:
        msg = '密码输入错误，请重新输入！'.format(teacher_name)
        teacher_logger.debug(msg)
        return False, msg


def select_course_interface(teacher_name, course_name):
    # 1.判断讲师是否选择课程
    teacher_obj = models.Teacher.select(teacher_name)
    if teacher_obj.course:
        msg = '讲师「{}」已经选择课程「{}」！'.format(teacher_name, teacher_obj.course)
        teacher_logger.debug(msg)
        return False, msg
    # 2.修改讲师对象课程属性
    teacher_obj.select_course(course_name)
    msg = '讲师「{}」选择课程「{}」成功'.format(teacher_name, course_name)
    teacher_logger.info(msg)
    return True, msg


def check_student_interface(teacher_name):
    # 1.判断讲师是否选择课程
    teacher_obj = models.Teacher.select(teacher_name)
    course_name = teacher_obj.course
    if not course_name:
        msg = '讲师「{}」请先选择课程！'.format(teacher_name)
        teacher_logger.debug(msg)
        return False, msg
    # 2.判断该课程是否有学生选择
    course_obj = models.Course.select(course_name)
    return True, course_obj.student_list


def modify_grade_interface(teacher_name, student_name, grade):
    teacher_obj = models.Teacher.select(teacher_name)
    teacher_obj.modify_grade(student_name, grade)
    msg = '讲师「{}」修改学生「{}」成绩为「{}」'.format(teacher_name, student_name, grade)
    teacher_logger.info(msg)
