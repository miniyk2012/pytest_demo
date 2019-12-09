import pytest

canshu = [{'usr': 'yangkai', 'pwd': '123'},
          {'usr': 'yewei', 'pwd': ''},
          ]


@pytest.fixture(scope="class")
def login(request):
    print("Enter")
    user = request.param['usr']
    pwd = request.param['pwd']
    if pwd != '':
        yield True
    else:
        yield False
    print("Exit")


@pytest.mark.parametrize('login', canshu, indirect=True)
class TestXX:
    def test_01(self, login):
        result = login
        assert result is True

    def test_02(self, login):
        result = login
        print('aaaaa')
        if not result:
            pytest.xfail('test_02登录不成功')
        assert result is True

    def test_03(self, login):
        assert 1 == 1
