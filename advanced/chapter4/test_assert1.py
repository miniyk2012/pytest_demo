# content of test_assert1.py

import pytest


def f():
    return


def test_function():
    assert f() == 4, "value was odd, should be even"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()

        f()
    print(type(excinfo.value))  # 实际抛出的异常RecursionError
    print(excinfo.type)  # 实际抛出的异常RecursionError
    # print(excinfo.traceback)
    assert "maximum recursion" in str(excinfo.value)


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()


@pytest.mark.xfail(raises=IndexError)
def test_xfail():
    def f():
        a = []
        a[1]

    f()
