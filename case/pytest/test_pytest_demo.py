# -*- coding:utf-8 -*-

import os
import pytest


def test_cmd_0():
    ''' the test cmd '''
    print('\nthe test_cmd_0 ended.')


if __name__ == "__main__":
    ''' the main point '''
    retcode = pytest.main(args=['-v', '-s', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--fixtures', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--collect-only', os.path.abspath(__file__)])
    print(retcode)
