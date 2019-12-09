import smtplib

import pytest


@pytest.fixture()
def smtp():
    # 由于环境问题, 因此连不上
    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp:
            yield smtp
            # 如果抛异常了，那么这里的teardown执行不到
            print('yield tear down')
    finally:
        # 用这里的finally一定可以执行到
        print('tear down')

def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
