import pytest


@pytest.fixture(scope="module", params=[('a', 'b')])
def smtp_connection(request):
    server = getattr(request.module, "smtpserver", "smtp.gmail.com")
    print('param', request.param)
    def fin():
        print("teardown smtp_connection")

    request.addfinalizer(fin)
    return server  # provide the fixture value


def test1(smtp_connection):
    print()
    print(smtp_connection)
    print('test1')


def test2(smtp_connection):
    print()
    print(smtp_connection)
    print('test2')
