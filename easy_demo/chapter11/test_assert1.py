import pytest
from _pytest._code import ExceptionInfo


def f():
    return 3


def test_f():
    a = f()
    assert a % 2 == 0, "判断a为偶数，当前a的值为：%s" % a

def test_raise():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1 / 0
    assert isinstance(excinfo, ExceptionInfo)
    assert excinfo.type == ZeroDivisionError
    assert isinstance(excinfo.value, ZeroDivisionError)
    assert "division by zero" == str(excinfo.value)
