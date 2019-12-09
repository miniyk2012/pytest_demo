import pytest

@pytest.fixture(scope="session")
def open_baidu(start):
    print("打开百度页面_session")
    return start