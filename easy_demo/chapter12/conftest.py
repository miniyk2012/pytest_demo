import sys
import pytest

platform_skip = pytest.mark.skipif(sys.platform == 'win32', reason="does not run on windows")
