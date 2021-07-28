# 数据处理层

import os
import pickle

from conf import settings


def save(obj):
    """将对象以bytes类型序列化保存到文件中"""
    class_name = obj.__class__.__name__
    class_dir = os.path.join(settings.BASE_PATH, 'db', class_name)
    if not os.path.exists(class_dir):
        os.mkdir(class_dir)
    file = os.path.join(class_dir, obj.name)
    with open(file, 'wb') as f:
        pickle.dump(obj, f)


def select(cls, name):
    """将文件中以bytes类型保存的对象反序列化返回"""
    class_name = cls.__name__
    file = os.path.join(settings.BASE_PATH, 'db', class_name, name)
    if not os.path.exists(file):
        return None
    with open(file, 'rb') as f:
        return pickle.load(f)
