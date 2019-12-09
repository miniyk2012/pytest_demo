import pytest


@pytest.fixture(scope="session")
def fix1():
    print('fix1 start')
    yield 1
    print('fix1 end')


@pytest.fixture()
def fix2(fix1):
    print('fix2 start')
    yield fix1 + 1
    print('fix2 end')

@pytest.fixture()
def fix3(fix1):
    print('fix3 start')
    yield fix1 + 2
    print('fix2 end')


def test1(fix1):
    print(f'test1={fix1}')
    assert fix1 == 1


def test2(fix1):
    print(f'test2={fix1}')
    assert fix1 == 1


def test3(fix2):
    print(f'test3={fix2}')
    assert fix2 == 2


def test4(fix2):
    print(f'test3={fix2}')
    assert fix2 == 2


def test5(fix1, fix3, fix2):
    print(f'test5: fix1={fix1}, fix2={fix2}, fix3={fix3}')
    assert fix1 == 1
    assert fix2 == 2
    assert fix3 == 3


