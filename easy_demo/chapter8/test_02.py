import time


def test_yoyo_02(browser):
    browser.get("https://www.cnblogs.com/yoyoketang/")
    # time.sleep(2)
    t = browser.title
    assert "上海-悠悠" in t
