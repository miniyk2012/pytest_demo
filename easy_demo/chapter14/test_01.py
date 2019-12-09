import pytest


class Model:
    pass


@pytest.fixture
def my_thing():
    class ThingFactory:
        def get(self):
            return Model()

    return ThingFactory()


def test1(my_thing):
    a = my_thing.get()
    b = my_thing.get()
    assert a != b
    assert id(a) != id(b)
