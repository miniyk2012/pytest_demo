import pytest

# 不带参数时默认scope="function"
@pytest.fixture()
def login():
    print("输入账号，密码先登录***********")