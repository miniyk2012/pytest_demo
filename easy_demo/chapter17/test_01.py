import pytest


@pytest.fixture(scope="class")
def start(request):
    print('\n-----开始执行function----')


def test_a(start):
    print("-------用例a执行-------")


class TestAAA:

    def test_01(self, start):
        print('-----------用例01--------------')

    def test_02(self, start):
        print('-----------用例02------------')
