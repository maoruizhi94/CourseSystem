# 管理员接口层

from lib import common
from db import models

admin_logger = common.customize_logger('admin')


def register_interface(admin_name, password):
    """管理员注册接口，创建管理员对象，返回flag和msg

    flag：注册成功标识符
    msg： 注册相关提示信息
    """
    # 1.判断用户是否存在
    if models.Admin.select(admin_name):
        msg = '「{}」已存在！'.format(admin_name)
        admin_logger.debug(msg)
        return False, msg
    # 2.注册管理员账号
    admin_obj = models.Admin(admin_name, password)
    admin_obj.save()
    msg = '管理员「{}」注册成功'.format(admin_name)
    admin_logger.info(msg)
    return True, msg


def login_interface(admin_name, password):
    """管理员登录接口，返回flag和msg

    flag：登录成功标识符
    msg： 登录相关提示信息
    """
    # 1.判断用户是否存在
    admin_obj = models.Admin.select(admin_name)
    if not admin_obj:
        msg = '「{}」不存在，请重新输入！'.format(admin_name)
        admin_logger.debug(msg)
        return False, msg
    # 2.判断密码是否正确
    if admin_obj.password == password:
        msg = '「{}」登录成功'.format(admin_name)
        admin_logger.debug(msg)
        return True, msg
    else:
        msg = '密码输入错误，请重新输入！'.format(admin_name)
        admin_logger.debug(msg)
        return False, msg


def create_school_interface(admin_name, school_name, school_addr):
    """创建校区对象，返回flag和msg

    flag：创建校区成功标识符
    msg： 相关提示信息
    """
    # 1.查看校区是否已经创建
    school_obj = models.School.select(school_name)
    if school_obj:
        msg = '「{}」已存在！'.format(school_name)
        admin_logger.debug(msg)
        return False, msg
    # 2.创建校区
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_school(school_name, school_addr)
    msg = '校区「{}」创建成功'.format(school_name)
    admin_logger.info(msg)
    return True, msg


def create_course_interface(admin_name, school_name, course_name):
    """创建课程对象，返回flag和msg

    flag：创建课程成功标识符
    msg： 相关提示信息
    """
    # 1.查看课程是否已经创建
    course_name = school_name + '-' + course_name
    course_obj = models.Course.select(course_name)
    if course_obj:
        msg = '「{}」已存在！'.format(course_name)
        admin_logger.debug(msg)
        return False, msg
    # 2.创建课程
    admin_obj = models.Admin.select(admin_name)
    school_obj = models.School.select(school_name)
    admin_obj.create_course(school_obj, course_name)
    msg = '课程「{}」创建成功'.format(course_name)
    admin_logger.info(msg)
    return True, msg


def create_teacher_interface(admin_name, teacher_name, pwd='123'):
    """创建讲师对象，返回flag和msg

    flag：创建讲师成功标识符
    msg： 相关提示信息
    """
    # 1.判断老师是否已经存在
    teacher_obj = models.Teacher.select(teacher_name)
    if teacher_obj:
        msg = '「{}」已存在！'.format(teacher_name)
        admin_logger.debug(msg)
        return False, msg
    # 2.创建老师对象
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name, pwd)
    msg = '讲师「{}」创建成功'.format(teacher_name)
    admin_logger.info(msg)
    return True, msg
