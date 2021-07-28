# 学生接口层

from lib import common
from db import models

student_logger = common.customize_logger('student')


def register_interface(student_name, student_password):
    """注册学生对象，返回flag和msg

    flag：注册成功标识符
    msg： 注册相关提示信息
    """
    # 1.判断用户是否存在
    if models.Student.select(student_name):
        msg = '「{}」已存在！'.format(student_name)
        student_logger.debug(msg)
        return False, msg
    # 2.注册学生账号
    student_obj = models.Student(student_name, student_password)
    student_obj.save()
    msg = '学生「{}」注册成功'.format(student_name)
    student_logger.info(msg)
    return True, msg


def login_interface(student_name, student_password):
    """学生登录接口，返回flag和msg

    flag：登录成功标识符
    msg： 登录相关提示信息
    """
    # 1.判断用户是否存在
    student_obj = models.Student.select(student_name)
    if not student_obj:
        msg = '「{}」不存在，请重新输入！'.format(student_name)
        student_logger.debug(msg)
        return False, msg
    # 2.判断密码是否正确
    if student_obj.password == student_password:
        msg = '「{}」登录成功'.format(student_name)
        student_logger.debug(msg)
        return True, msg
    else:
        msg = '密码输入错误，请重新输入！'.format(student_name)
        student_logger.debug(msg)
        return False, msg


def select_school_interface(student_name, school_name):
    """学生选择校区接口，修改学生对象校区属性，返回flag和msg

    flag：成功标识符
    msg： 相关提示信息
    """
    student_obj = models.Student.select(student_name)
    if student_obj.school:
        msg = '「{}」已经选择校区「{}」!'.format(student_name, student_obj.school)
        student_logger.debug(msg)
        return False, msg
    student_obj.select_school(school_name)
    msg = '学生「{}」选择校区「{}」成功'.format(student_name, school_name)
    student_logger.info(msg)
    return True, msg


def select_course_interface(student_name):
    """修改学生对象course属性"""
    # 1.判断学生是否选择校区
    student_obj = models.Student.select(student_name)
    school_name = student_obj.school
    if not school_name:
        msg = '「{}」请先选择校区!'.format(student_name)
        student_logger.debug(msg)
        return False, msg
    if student_obj.course:
        msg = '「{}」已经选择课程「{}」!'.format(student_name, student_obj.course)
        student_logger.debug(msg)
        return False, msg
    # 2.打印该校区所有课程让学生选择
    school_obj = models.School.select(school_name)
    for index, course_name in enumerate(school_obj.course_list):
        print(index, course_name)
    index = input('请输入课程编号：').strip()
    course_name = school_obj.course_list[int(index)]
    student_obj.select_course(course_name, student_name)
    msg = '学生「{}」选择课程「{}」成功'.format(student_name, course_name)
    student_logger.info(msg)
    return True, msg


def check_grade_interface(student_name):
    student_obj = models.Student.select(student_name)
    student_course = student_obj.course
    if not student_course:
        msg = '「{}」还没有选择课程!'.format(student_name)
        student_logger.debug(msg)
        return False, msg
    student_grade = student_obj.grade
    msg = '课程：{} 成绩：{}'.format(student_course, student_grade)
    student_logger.debug(msg)
    return True, msg
