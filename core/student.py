# 学生视图层

from core import common as core_common
from lib import common as lib_common
from interface import student_interface, common_interface

student_info = {'username': ''}


def register():
    """学生注册功能"""
    core_common.register(student_interface)


def login():
    """学生登录功能"""
    core_common.login(student_interface, student_info)


@lib_common.login_auth('student')
def select_school():
    """学生选择校区"""
    while True:
        # 1.展示所有校区让学生选择
        school_list = common_interface.display_school_interface()
        if not school_list:
            print('请联系管理员创建校区！')
            break
        for index, school in enumerate(school_list):
            print(index, school)
        index = input('请输入校区编号：').strip()
        if not index.isdigit():
            print('请输入正确的编号！')
            continue
        index = int(index)
        if index not in range(len(school_list)):
            print('请输入正确的编号！')
            continue
        school_name = school_list[index]
        # 2.调用选择校区接口
        student_name = student_info.get('username')
        flag, msg = student_interface.select_school_interface(student_name, school_name)
        print(msg)
        break


@lib_common.login_auth('student')
def select_course():
    """学生选择课程"""
    student_name = student_info.get('username')
    flag, msg = student_interface.select_course_interface(student_name)
    print(msg)


def check_grade():
    """学生查看课程对应的成绩"""
    student_name = student_info.get('username')
    flag, msg = student_interface.check_grade_interface(student_name)
    print(msg)


num_func = {
    '1': register,
    '2': login,
    '3': select_school,
    '4': select_course,
    '5': check_grade,
}


def student_view():
    while True:
        print("""
                学生视图
                0  退出
                1  注册功能
                2  登录功能
                3  选择校区功能
                4  选择课程功能
                5  查看成绩功能""")
        number = input('请输入编号🦋：').strip()
        if number == '0':
            print('退出学生视图')
            return
        if number not in num_func:
            print('请输入正确的编号！')
            continue
        num_func.get(number)()
