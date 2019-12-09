import pytest


@pytest.fixture(scope="module")
def input_user(request):
    user = request.param
    print("登录账户：%s" % user)
    return user


@pytest.fixture(scope="module")
def input_psw(request):
    psw = request.param
    print("登录密码：%s" % psw)
    return psw


test_user = ["admin1", "admin2"]
test_psw = ["11111", "22222"]


@pytest.mark.parametrize('input_user', test_user, indirect=True)
@pytest.mark.parametrize('input_psw', test_psw, indirect=True)
def test_login(input_user, input_psw):
    print(input_user, input_psw)
