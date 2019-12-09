# content of conftest.py
import pytest
import pdb


def pytest_addoption(parser):  # 这是个钩子,函数名和参数名必须是这个值
    print("parse:", parser)
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")
