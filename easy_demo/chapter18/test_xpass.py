import pytest

def test_hello():
    print("hello world!")
    assert 1

@pytest.mark.xfail(reason="a不等于b")
def test_yoyo1():
    a = "hello"
    b = "hello world"
    assert a == b

@pytest.mark.xfail()
def test_yoyo2():
    """希望失败, 但却成功了"""
    a = "hello"
    b = "hello world"
    assert a != b
