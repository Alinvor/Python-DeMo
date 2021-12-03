# -*- coding:utf-8 -*-

import os
import pytest


def test_xxx():
    ''' the test case method '''
    pass


if __name__ == "__main__":
    ''' the pytest main point '''
    retcode = pytest.main(args=['-v', '-s', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--fixtures', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--collect-only', os.path.abspath(__file__)])
    print(retcode)
