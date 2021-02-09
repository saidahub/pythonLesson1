# fixture 参数化使用
# 使用param 参数化时想要获取返回值时，必须用request.param 且不可更改
import pytest


@pytest.fixture(params=["herry", "hemin"])
def login(request):
    print("登录")
    return request.param


def test_serch(login):
    print(login)
    print("搜索")
