import pytest
from loguru import logger


# fixture参数化的2种方法

# 法1, param放在test case上面
@pytest.fixture()
def login(request):
    user = request.param
    return user


@pytest.mark.parametrize('login', ['yangkai', 'xiaojian'], indirect=True)
def test_open(login):
    logger.info(login)


# 法2: param放在fixture的上面
@pytest.fixture(params=[
    ('redis', '6379'),
    ('elasticsearch', '9200')
])
def db(request):
    param = request.param
    logger.info('\nSucceed to connect %s:%s' % param)

    yield param

    logger.info('\nSucceed to close %s:%s' % param)


def test_api(db):
    logger.info(f'name={db[0]}, port={db[1]}')
