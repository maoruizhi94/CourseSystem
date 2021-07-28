# 管理员视图层

from core import common as core_common
from lib import common as lib_common
from interface import admin_interface, common_interface

admin_info = {'username': ''}


def register():
    """管理员注册功能"""
    core_common.register(admin_interface)


def login():
    """管理员登录功能"""
    core_common.login(admin_interface, admin_info)


@lib_common.login_auth('admin')
def create_school():
    """创建校区功能"""
    while True:
        admin_name = admin_info.get('username')
        school_name = input('请输入校区名称：').strip()
        school_addr = input('请输入校区地址：').strip()
        if len(school_name) == 0 or len(school_addr) == 0:
            print('校区名和地址不能为空!')
            continue
        flag, msg = admin_interface.create_school_interface(admin_name, school_name, school_addr)
        print(msg)
        break


@lib_common.login_auth('admin')
def create_course():
    """给指定校区创建课程"""
    while True:
        # 1.展示所有校区让管理员选择
        school_list = common_interface.display_school_interface()
        if not school_list:
            print('请先创建校区！')
            return
        for index, school in enumerate(school_list):
            print(index, school)
        index = input('请先输入校区编号：').strip()
        if not index.isdigit():
            print('请输入正确的编号！')
            continue
        index = int(index)
        if index not in range(len(school_list)):
            print('请输入正确的编号！')
            continue
        school_name = school_list[index]
        # 2.指定校区创建课程
        admin_name = admin_info.get('username')
        course_name = input('请输入课程名称：').strip()
        if course_name == '':
            print('课程名称不能为空！')
            continue
        flag, msg = admin_interface.create_course_interface(
            admin_name,
            school_name,
            course_name,
        )
        print(msg)
        break


@lib_common.login_auth('admin')
def create_teacher():
    """创建讲师功能"""
    while True:
        admin_name = admin_info.get('username')
        teacher_name = input('请输入老师姓名：').strip()
        if teacher_name == '':
            print('输入不能为空！')
            continue
        flag, msg = admin_interface.create_teacher_interface(admin_name, teacher_name)
        print(msg)
        break


num_func = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_course,
    '5': create_teacher,
}


def admin_view():
    while True:
        print("""
            管理员视图
            0  退出
            1  注册功能
            2  登录功能
            3  创建校区功能
            4  创建课程功能
            5  创建讲师功能""")
        number = input('请输入编号：').strip()
        if number == '0':
            print('退出管理员视图')
            return
        if number not in num_func:
            print('请输入正确的编号！')
            continue
        num_func.get(number)()
