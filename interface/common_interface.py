# 共享接口层

import os

from conf import settings


def display_school_interface():
    """返回所有校区列表或者None"""
    school_dir = os.path.join(settings.BASE_PATH, 'db', 'School')
    if os.path.exists(school_dir):
        return os.listdir(school_dir)
    else:
        return None


def display_course_interface():
    """返回所有课程列表或者None"""
    course_dir = os.path.join(settings.BASE_PATH, 'db', 'Course')
    if os.path.exists(course_dir):
        return os.listdir(course_dir)
    else:
        return None
