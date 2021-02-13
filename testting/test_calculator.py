import sys
import pytest
import yaml
#
# sys.path.append('..')
# print(sys.path)

from pythoncode.calculator import Calculator


def get_datas(name, type='int'):
    with open("./data/calc.yml",encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
        datas = all_datas[name][type]['datas']
        ids = all_datas[name][type]['ids']
        return (datas, ids)


# 测试类
class TestCalc:
    # 定义类变量
    # datas: list= get_datas()
    add_int_data = get_datas('add', 'int')
    print(add_int_data)
    add_float_data = get_datas('add', 'float')
    print(add_float_data)

    div_int_data = get_datas('div', 'int')
    print(div_int_data)
    div_float_data = get_datas('div', 'float')
    print(div_float_data)
    div_abnormal_data = get_datas('div', 'abnormal')
    print(div_abnormal_data)

    # 前置条件

    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()  # 实例化对象

    def teardown_class(self):
        print("结束计算")

    # 整数相加
    @pytest.mark.parametrize("a, b, result", add_int_data[0], ids=add_int_data[1])
    @pytest.mark.add
    def test_add_int(self, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        assert result == self.calc.add(a, b)

    # 浮点数相加
    @pytest.mark.parametrize("a, b, result", add_float_data[0], ids=add_float_data[1])
    def test_add_float(self, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        # round()方法保留小数点后的位数
        assert result == round(self.calc.add(a, b), 2)

    # todo: 相除功能
    @pytest.mark.parametrize("a, b, result", div_int_data[0], ids=div_int_data[1])
    @pytest.mark.div
    def test_div_int(self, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        assert result == self.calc.div(a, b)

    # 浮点数测试用例设计
    @pytest.mark.parametrize("a, b, result", div_float_data[0], ids=div_float_data[1])
    def test_div_float(self, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        assert result == round(self.calc.div(a, b), 2)

    # 异常情况测试用例设计
    @pytest.mark.parametrize("a, b, result", div_abnormal_data[0], ids=div_abnormal_data[1])
    def test_div_abnormal(self, a, b, result):
        with pytest.raises(ZeroDivisionError):
            assert result == self.calc.div(a, b)
            print("除数不能为0")
