import pytest


@pytest.fixture()
def user():
    print("获取用户名")
    a = "yoyo"
    return a


@pytest.fixture()
def fixture_error():
    print("获取用户名")
    a = "yoyo"
    assert a == "yoyo123"  # fixture失败就是error
    return a


def test_1(user):
    assert user == "yoyo111"  # 用例失败就是failed


def test_2(fixture_error):
    assert user == "yoyo111"
