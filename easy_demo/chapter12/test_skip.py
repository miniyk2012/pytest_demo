import pytest
from easy_demo.chapter12.conftest import platform_skip



@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    assert False


def valid_config():
    return False


@pytest.mark.xfail(reason="should fail")
def test_xfail():
    assert False


@pytest.mark.xfail(reason="should fail")
def test_xpass():
    assert True

def test_function1():
    if not valid_config():
        pytest.skip("unsupported configuration")
    assert False


@platform_skip
def test_function2():
    assert False


@platform_skip
class TestPosixCalls:
    def test_function(self):
        "will not be setup or run under 'win32' platform"
        assert False

def test_function3():
    assert False

# 写了下面这行, 则该模块所有case都跳过
# pytestmark = pytest.mark.skip
