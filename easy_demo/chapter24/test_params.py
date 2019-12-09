import pytest

"""多个数据的测试用例也可以用这种方式来构造
"""
@pytest.fixture(params=(1, 2, 3))
def fix1(request):
    return request.param


def test1(fix1):
    print(fix1)
