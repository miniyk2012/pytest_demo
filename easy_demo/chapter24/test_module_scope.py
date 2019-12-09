import pytest

@pytest.fixture(scope="module")
def first():
    print("\n获取用户名,scope为module级别当前.py模块只运行一次")
    a = "yoyo"
    return a


def test_1(first):
    '''用例传fixture'''
    print("测试账号：%s" % first)
    assert first == "yoyo"

class TestCase():
    def test_2(self, first):
        '''用例传fixture'''
        print("测试账号：%s" % first)
        assert first == "yoyo"
