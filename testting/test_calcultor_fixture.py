import sys
import pytest
import yaml
#
# sys.path.append('..')
# print(sys.path)

from pythoncode.calculator import Calculator


def get_datas(name, type='int'):
    with open("./data/calc.yml") as f:
        all_datas = yaml.safe_load(f)
        datas = all_datas[name][type]['datas']
        ids = all_datas[name][type]['ids']
        return (datas, ids)


# 添加一个fixture 相当于setup teardown
@pytest.fixture()
def get_instance():
    print("开始计算")
    calc: list = Calculator()
    yield calc
    print("结束计算")


@pytest.fixture(params=[get_datas('add', 'int')[0], get_datas('add', 'float')[0]],
                ids=[get_datas('add', 'int')[1], get_datas('add', 'float')[1]])
def get_calc_with_fixture(request):
    return request.param


def test_param(get_calc_with_fixture):
    print(get_calc_with_fixture)


# 测试类
class TestCalc:
    # 定义类变量
    # datas: list= get_datas()
    # add_int_data = get_datas('add', 'int')
    # print(add_int_data)
    # add_float_data = get_datas('add', 'float')
    # print(add_float_data)

    div_int_data = get_datas('div', 'int')
    print(div_int_data)
    div_float_data = get_datas('div', 'float')
    print(div_float_data)
    div_abnormal_data = get_datas('div', 'abnormal')
    print(div_abnormal_data)

    # 整数相加
    #    @pytest.mark.parametrize("a, b, result", add_int_data[0], ids=add_int_data[1])
    @pytest.mark.add
    def test_add_int(self, get_instance, get_calc_with_fixture):
        f = get_calc_with_fixture
        print(f)
        assert f[0][2] == get_instance.add(f[0][0], f[0][1])

    # 浮点数相加
    #    @pytest.mark.parametrize("a, b, result", add_float_data[0], ids=add_float_data[1])
    #     def test_add_float(self, get_instance, get_calc_with_fixture):
    #         f= get_calc_with_fixture
    #         # round()方法保留小数点后的位数
    #         assert f[1][2] == round(get_instance.add(f[1][0], f[1][1]), 2)

    # todo: 相除功能
    @pytest.mark.parametrize("a, b, result", div_int_data[0], ids=div_int_data[1])
    @pytest.mark.div
    def test_div_int(self, get_instance, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        assert result == get_instance.div(a, b)

    # 浮点数测试用例设计
    @pytest.mark.parametrize("a, b, result", div_float_data[0], ids=div_float_data[1])
    def test_div_float(self, get_instance, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        assert result == round(get_instance.div(a, b), 2)

    # 异常情况测试用例设计
    @pytest.mark.parametrize("a, b, result", div_abnormal_data[0], ids=div_abnormal_data[1])
    def test_div_abnormal(self, get_instance, a, b, result):
        with pytest.raises(ZeroDivisionError):
            assert result == get_instance.div(a, b)
            print("除数不能为0")
