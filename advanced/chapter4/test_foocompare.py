class Foo:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2


def test_compare2():
    class B:
        val = 10
    f1 = Foo(1)
    f2 = B
    assert f1 == f2
