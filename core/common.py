# 共享视图层

def register(interface):
    """注册功能

    注册成功，回到视图主函数；
    注册失败，打印失败信息，继续注册。
    """
    while True:
        name = input('请设置用户名：').strip()
        password = input('请设置登录密码：').strip()
        confirm_password = input('请输入确认密码：').strip()
        if len(name) == 0 or len(password) == 0:
            print('用户名和密码不能为空!')
            continue
        if not password == confirm_password:
            print('密码不一致，请重新输入！')
            continue
        flag, msg = interface.register_interface(name, password)
        print(msg)
        break


def login(interface, user_info):
    """登录功能

    登录成功，修改全局登录标识符，回到视图主函数；
    登录失败，打印失败信息，继续登录。
    """
    while True:
        name = input('请输入用户名：').strip()
        password = input('请输入登录密码：').strip()
        if len(name) == 0 or len(password) == 0:
            print('用户名和密码不能为空!')
            continue
        flag, msg = interface.login_interface(name, password)
        if flag:
            user_info['username'] = name  # 登录成功标识符
            print(msg)
            return
        else:
            print(msg)
