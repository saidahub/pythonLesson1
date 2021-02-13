import pytest


# @pytest.mark.flaky(reruns=5,reruns_delay=2)
# 多个断言都执行的语法pytest.assume()
def test_rerun():
    pytest.assume(1 == 2)
    pytest.assume(1 == 1)
    pytest.assume(2 == 3)