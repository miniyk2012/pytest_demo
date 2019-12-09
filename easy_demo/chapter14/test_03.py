"""Pytest will only cache one instance of a fixture at a time.
This means that when using a parametrized fixture, pytest may invoke a fixture more than once in the given scope."""

import pytest

# 测试账号数据
test_user_data = [{"user": "admin1", "psw": "111111"},
                  {"user": "admin2", "psw": ""}]


@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    psw = request.param["psw"]
    print("登录账户：%s" % user)
    print("登录密码：%s" % psw)
    if psw:
        return True
    else:
        return False


# indirect=True 声明login是个函数
@pytest.mark.parametrize("login", test_user_data, indirect=True)
def test_login(login):
    '''登录用例'''
    a = login
    print("测试用例中login的返回值:%s" % a)
    assert a, "失败原因：密码为空"


if __name__ == "__main__":
    pytest.main(["-s", "test_03.py"])
