import os
import sys


def here(module_name):
    filename = os.path.abspath(sys.modules[module_name].__file__)
    return os.path.abspath(os.path.dirname(filename))
