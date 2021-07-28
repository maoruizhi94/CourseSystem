from core import admin, student, teacher

num_func = {
    '1': admin.admin_view,
    '2': student.student_view,
    '3': teacher.teacher_view,
}


def main():
    """视图层主函数"""
    while True:
        print("""
            欢迎来到选课系统！
            0  退出
            1  管理员视图
            2  学生视图
            3  讲师视图""")
        number = input('请输入编号：').strip()
        if number == '0':
            print('退出选课系统！')
            return
        if number not in num_func:
            print('请输入正确的编号！')
            continue
        num_func.get(number)()
