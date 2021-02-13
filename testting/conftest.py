# python的一个配置文件，文件名固定，且不能修改，主要定义公共内容
# 主要存放fixture
'''
可以存放fixture , hook 函数
就近生效（如果不在同一个文件夹下，离测试文件最近的conftest.py 生效）
当前目录一定要有__init__.py 文件，也就是要创建一个包
'''

import datetime
from typing import List

import pytest

from pythoncode.calculator import Calculator


@pytest.fixture()
def login():
    print("登录操作")
    #   token = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    token = datetime.datetime.now()
    # yield相当于return 返回yield前的结果，yield 后的操作输出在teardown中
    yield token
    print("登出操作")


@pytest.fixture(scope="module")
def get_instance():
    print("开始计算")
    calc: list = Calculator()
    yield calc
    print("结束计算")


# hook 函数改写时测试数据中的ids 命名改成中文
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')