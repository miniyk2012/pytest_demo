import os

from dunder_demo.package1 import *
from dunder_demo import package1

print('usage', A)
package1.A = 55
print(B)
print(package1.C)
import calendar
print(calendar.January)
calendar.January = 13


from multiprocessing.process import _process_counter
print(_process_counter)
next(_process_counter)  # 改变了全局变量的状态
next(_process_counter)  # 改变了全局变量的状态

from dunder_demo import package_usage2

import glob
from json.encoder import HAS_UTF8







