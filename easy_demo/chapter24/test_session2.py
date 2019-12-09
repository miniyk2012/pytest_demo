def test_1(module_fixture):
    '''用例2传fixture'''
    print("测试账号：%s" % module_fixture)
    assert module_fixture == "yoyo"
