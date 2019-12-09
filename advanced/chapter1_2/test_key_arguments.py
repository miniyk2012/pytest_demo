import pytest


@pytest.mark.parametrize("args, kwargs, expecting", [
    ([100, 10], {'c': True}, (90, 110)),
    ([100, .2], {'c': False}, (80, 120)),
])
def test_fn(args, kwargs, expecting):
    print(args, kwargs)
    assert fn(*args, **kwargs) == expecting


def fn(a, b, c=False):
    if c:
        return a - b, a + b
    else:
        return a - (a * b), a + a * b


def move_zeros(nums):
    length = len(nums)
    i, j = 0, 0
    while i < length:
        if nums[j] == 0:
            nums.pop(j)
        else:
            j += 1
        i += 1
    for m in range(i - j):
        nums.append(0)


def test_move_zeros():
    nums = [0, -4, 0, 0, 6, 10, 0, 1]
    move_zeros(nums)
    nums == [-4, 6, 10, 1, 0, 0, 0, 0]
