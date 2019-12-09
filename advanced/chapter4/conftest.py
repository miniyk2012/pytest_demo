import pytest
from test_foocompare import Foo


# 自定义assert解释, 在reporting中会打印出来(每个案例都会过一下这个, 如果返回空, 则使用默认结果)
def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return ["WAWA Comparing Foo instances:",
                " vals: {} != {}".format(left.val,
                                         right.val),
                ]

pytest.register_assert_rewrite("helper")  # Assertion Rewriting
