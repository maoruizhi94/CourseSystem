from logging import config, getLogger
from functools import wraps

from conf import settings


def login_auth(view_name):
    """登录认证装饰器

    若用户未登录，则跳转到登录功能。
    """

    def decorator(func):

        from core import admin, student, teacher

        @wraps(func)
        def wrapper(*args, **kwargs):
            if view_name == 'admin':
                if admin.admin_info.get('username'):
                    return func(*args, **kwargs)
                else:
                    print('请先登录!')
                    admin.login()
            elif view_name == 'student':
                if student.student_info.get('username'):
                    return func(*args, **kwargs)
                else:
                    print('请先登录!')
                    student.login()
            elif view_name == 'teacher':
                if teacher.teacher_info.get('username'):
                    return func(*args, **kwargs)
                else:
                    print('请先登录!')
                    teacher.login()

        return wrapper

    return decorator


def customize_logger(logger_name):
    """自定义日志器"""
    config.dictConfig(settings.LOGGING_DICT)
    return getLogger(logger_name)
