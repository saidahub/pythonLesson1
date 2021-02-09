# fixture 用法学习
import pytest


@pytest.fixture()
def login():
    print("登录操作")


# fixture可调用fixture
@pytest.fixture()
def get_username(login):
    name = '赫敏'
    print(name)
    return name


def test_search(login):
    print("搜索")


def test_cart(login):
    print("购物")


# 多个fixture调用 用装饰器调用时，被调用的方法名需要用双引号
# 多个fixture时写多个装饰器 调用顺序是由内往外
@pytest.mark.usefixtures("get_username")
@pytest.mark.usefixtures("login")
def test_order():
    print("下单")
