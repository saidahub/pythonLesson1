
from pythoncode.calculator import Calculator
import allure
import pytest
import yaml


def get_datas(name, type='int'):
    with open("./data/calc.yml", encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
        datas = all_datas[name][type]['datas']
        ids = all_datas[name][type]['ids']
        return (datas, ids)


# # 添加一个fixture 相当于setup teardown
# @pytest.fixture(scope="module")
# def get_instance():
#     print("开始计算")
#     calc: list = Calculator()
#     yield calc
#     print("结束计算")


# fixture中的params和ids 当数据有多组时需要分开写，不能写在一个里面
@pytest.fixture(params=get_datas('add', 'int')[0], ids=get_datas('add', 'int')[1])
def get_calc_with_fixture_int(request):
    return request.param


@pytest.fixture(params=get_datas('add', 'float')[0], ids=get_datas('add', 'float')[1])
def get_calc_with_fixture_float(request):
    return request.param


@pytest.fixture(params=get_datas('div', 'int')[0], ids=get_datas('div', 'int')[1])
def get_calc_with_fixture_div_int(request):
    return request.param


@pytest.fixture(params=get_datas('div', 'float')[0], ids=get_datas('div', 'float')[1])
def get_calc_with_fixture_div_float(request):
    return request.param


@pytest.fixture(params=get_datas('div', 'abnormal')[0], ids=get_datas('div', 'abnormal')[1])
def get_calc_with_fixture_div_abnormal(request):
    return request.param


# 测试类
@allure.feature("计算器")
class TestCalc:
    # 定义类变量
    # datas: list= get_datas()
    # add_int_data = get_datas('add', 'int')
    # print(add_int_data)
    # add_float_data = get_datas('add', 'float')
    # print(add_float_data)

    # div_int_data = get_datas('div', 'int')
    # print(div_int_data)
    # div_float_data = get_datas('div', 'float')
    # print(div_float_data)
    # div_abnormal_data = get_datas('div', 'abnormal')
    # print(div_abnormal_data)

    # 整数相加
    #    @pytest.mark.parametrize("a, b, result", add_int_data[0], ids=add_int_data[1])
    @allure.story("整数相加功能")
    @pytest.mark.add
    def test_add_int(self, get_instance, get_calc_with_fixture_int):
        i = get_calc_with_fixture_int
        print(i)
        assert i[2] == get_instance.add(i[0], i[1])

    # 浮点数相加
    #    @pytest.mark.parametrize("a, b, result", add_float_data[0], ids=add_float_data[1])
    @allure.story("浮点数数相加功能")
    def test_add_float(self, get_instance, get_calc_with_fixture_float):
        f = get_calc_with_fixture_float
        print(f)
        # round()方法保留小数点后的位数
        assert f[2] == round(get_instance.add(f[0], f[1]), 2)

    # todo: 相除功能
    #    @pytest.mark.parametrize("a, b, result", div_int_data[0], ids=div_int_data[1])#
    #    @allure.title("相加_{get_calc_with_fixture_div_int[0]}_{get_calc_with_fixture_div_int[1]}")
    @allure.story("整数相除功能")
    @pytest.mark.div
    def test_div_int(self, get_instance, get_calc_with_fixture_div_int):
        div_int = get_calc_with_fixture_div_int
        print(div_int)
        assert div_int[2] == get_instance.div(div_int[0], div_int[1])

    # 浮点数测试用例设计
    #    @pytest.mark.parametrize("a, b, result", div_float_data[0], ids=div_float_data[1])
    @allure.story("浮点数相除功能")
    def test_div_float(self, get_instance, get_calc_with_fixture_div_float):
        div_float = get_calc_with_fixture_div_float
        print(div_float)
        assert div_float[2] == round(get_instance.div(div_float[0], div_float[1]), 2)

    # 异常情况测试用例设计
#    @pytest.mark.parametrize("a, b, result", div_abnormal_data[0], ids=div_abnormal_data[1])
    @allure.story("异常情况相除")
    def test_div_abnormal(self, get_instance, get_calc_with_fixture_div_abnormal):
        with pytest.raises(ZeroDivisionError):
            div_abnormal = get_calc_with_fixture_div_abnormal
            print(div_abnormal)
            assert get_calc_with_fixture_div_abnormal[2] == get_instance.div(get_calc_with_fixture_div_abnormal[0],
                                                                             get_calc_with_fixture_div_abnormal[1])
            print("除数不能为0")
