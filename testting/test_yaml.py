import yaml


def test_yaml():
    # 打开文件
    with open("./data/calc.yml") as f:
        data = yaml.safe_load(f)
        print(data)
        print(data['add']['datas_int'])