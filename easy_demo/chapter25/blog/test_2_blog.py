def test_03(start, open_blog):
    print("测试用例test_03")
    assert 1

def test_04(start, open_blog):
    print("测试用例test_04")
    assert 1

def test_05(start, open_baidu):
    '''跨模块调用baidu模块下的conftest'''
    print("测试用例test_05,跨模块调用baidu")
    assert 1