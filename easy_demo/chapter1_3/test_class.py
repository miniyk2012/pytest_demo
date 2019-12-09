from pytest import mark


class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    @mark.slow
    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

    def test_three(self):
        a = "hello"
        b = "hello world"
        assert a in b
