# python的一个配置文件，文件名固定，且不能修改，主要定义公共内容
import datetime

import pytest


@pytest.fixture()
def login():
    print("登录操作")
    #   token = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    token = datetime.datetime.now()
    # yield相当于return 返回yield前的结果，yield 后的操作输出在teardown中
    yield token
    print("登出操作")