def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    print("setting up", item)


def pytest_runtest_teardown(item, nextitem):
    print('tearDown', item, nextitem)


def pytest_runtest_call(item):
    # 这样可以调用测试用例, 但这样会导致每个用例被调用2次
    item.runtest()


def pytest_collection_modifyitems(session, config, items):
    # called after collection is completed
    # you can modify the ``items`` list
    """试试看"""
    print(session)


def pytest_fixture_setup(fixturedef, request):
    print('before fixture_setup' + '****************')
    print(fixturedef)
    print(request)
    print('after fixture_setup' + '****************')


def pytest_fixture_post_finalizer(fixturedef, request):
    """ called after fixture teardown, but before the cache is cleared so
    the fixture result cache ``fixturedef.cached_result`` can
    still be accessed."""
    print('before fixture_post_finalizer' + '****************')
    print(fixturedef)
    print(request)
    print('after fixture_post_finalizer' + '****************')
