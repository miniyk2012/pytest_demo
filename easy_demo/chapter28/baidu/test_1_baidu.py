import time

import pytest

@pytest.mark.repeat(5)
def test_01(open_baidu):
    print("测试用例test_01")
    time.sleep(1)
    assert open_baidu == "yoyo"


def test_02(open_baidu):
    print("测试用例test_02")
    time.sleep(1)
    assert open_baidu == "yoyo"


if __name__ == "__main__":
    pytest.main(["-s", "test_1_baidu.py"])
