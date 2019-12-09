import pytest


def test_01(start, open_baidu):
    print("测试用例test_01")
    assert 1

@pytest.mark.repeat(5)
def test_02(start, open_baidu):
    print("测试用例test_02")
    assert 1
