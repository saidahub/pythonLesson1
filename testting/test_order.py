import pytest


# 不加order装饰器时从上往下执行，加了之后就按照装饰器定义的顺序执行
@pytest.mark.run(order=2)
def test_foo():
    assert True


@pytest.mark.run(order=1)
def test_bar():
    assert True
