import pytest


def test_sub1():
    print('sub1')


def test_sub2():
    print('sub2')


@pytest.fixture()
def login():
    return 10


def test_login(login):
    assert login == 10
    print('in test_login')
