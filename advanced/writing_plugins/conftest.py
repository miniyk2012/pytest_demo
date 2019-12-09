def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    print("root setting up", item)


import socket, logging, types
