import pytest
from selenium import webdriver
import os
import pdb
driver = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    ** 作者：上海-悠悠 QQ交流群：588402570**
    :param item:
    """
    # pdb.set_trace()

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            # pdb.set_trace()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclipck="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))

        report.extra = extra


def _capture_screenshot():
    '''
    截图保存为base64，展示到html中
    :return:
    '''
    return driver.get_screenshot_as_base64()


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    print('****************************************wawawaa******************')
    if driver is None:
        drive_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'chromedriver.exe')
        driver = webdriver.Chrome(drive_path)
    return driver
