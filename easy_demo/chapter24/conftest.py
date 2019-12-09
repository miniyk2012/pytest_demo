import pytest

@pytest.fixture(scope="session")
def module_fixture():
    print("\n获取用户名,scope为session级别多个.py模块只运行一次")
    a = "yoyo"
    return a