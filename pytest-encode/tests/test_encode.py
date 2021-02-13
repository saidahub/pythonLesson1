import pytest
from pytest_encode import logger


@pytest.mark.parametrize('name', ['哈利波特', '凯特'])
def test_encode(name):
    logger.info(f"测试数据： {name}")
    print(name)