# -*- coding:utf-8 -*-

import os
import pytest


@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit(object):
    ''' TestDirectoryInit '''
    def test_cwd_starts_empty(self):
        ''' test_cwd_starts_empty '''
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        ''' test_cwd_again_starts_empty '''
        assert os.listdir(os.getcwd()) == []


if __name__ == "__main__":
    ''' the main point '''
    retcode = pytest.main(args=['-v', '-s', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--fixtures', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--collect-only', os.path.abspath(__file__)])
    print(retcode)
