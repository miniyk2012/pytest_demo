import pytest
import math


@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.parametrize('testinput,expected',
                         [(4, 2),
                          (16, 4)
                          ])
def test_sqrt(testinput, expected):
    assert math.sqrt(testinput) == expected


@pytest.mark.parametrize('x', [0, 1])
@pytest.mark.parametrize('y', [102, 103])
def test_combine(x, y):
    print("测试数据组合：x->%s, y->%s" % (x, y))
