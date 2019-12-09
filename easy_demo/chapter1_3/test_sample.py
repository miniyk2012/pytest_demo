import pytest


def func(x):
    return x + 1


def test_answer1():
    assert func(3) == 4


def test_answer2():
    assert func(5) == 6


if __name__ == "__main__":
    pytest.main(['-v', 'test_sample.py'])
