# 讲师视图层

from core import common as core_common
from lib import common as lib_common
from interface import common_interface, teacher_interface

teacher_info = {'username': ''}


def login():
    """讲师登录功能"""
    core_common.login(teacher_interface, teacher_info)


@lib_common.login_auth('teacher')
def select_course():
    """讲师选择课程功能"""
    while True:
        # 1.打印所有课程让讲师选择
        course_list = common_interface.display_course_interface()
        if not course_list:
            print('请联系管理员创建课程！')
            break
        for index, course in enumerate(course_list):
            print(index, course)
        index = input('请输入课程编号：').strip()
        if not index.isdigit():
            print('请输入正确的编号！')
            continue
        index = int(index)
        if index not in range(len(course_list)):
            print('请输入正确的编号！')
            continue
        course_name = course_list[index]
        teacher_name = teacher_info.get('username')
        flag, msg = teacher_interface.select_course_interface(teacher_name, course_name)
        print(msg)
        break


@lib_common.login_auth('teacher')
def check_student():
    """打印讲师教授课程对应的学生名单"""
    teacher_name = teacher_info.get('username')
    flag, student_list = teacher_interface.check_student_interface(teacher_name)
    if flag:
        if not student_list:
            print('目前还没有学生报名')
        else:
            for index, student_name in enumerate(student_list):
                print(index, student_name)
    else:
        print(student_list)


@lib_common.login_auth('teacher')
def modify_grade():
    teacher_name = teacher_info.get('username')
    flag, student_list = teacher_interface.check_student_interface(teacher_name)
    if flag:
        if not student_list:
            print('目前还没有学生报名')
        else:
            for index, student_name in enumerate(student_list):
                print(index, student_name)
            index = input('请输入索引：').strip()
            student_name = student_list[int(index)]
            grade = int(input('请输入要修改的成绩：').strip())
            teacher_interface.modify_grade_interface(teacher_name, student_name, grade)
    else:
        print(student_list)


num_func = {
    '1': login,
    '2': select_course,
    '3': check_student,
    '4': modify_grade,
}


def teacher_view():
    while True:
        print("""
                讲师视图
                0  退出
                1  登录功能
                2  选择课程功能
                3  查看学生名单功能
                4  修改学生成绩功能""")
        number = input('请输入编号🦋：').strip()
        if number == '0':
            print('退出讲师视图')
            return
        if number not in num_func:
            print('请输入正确的编号！')
            continue
        num_func.get(number)()
