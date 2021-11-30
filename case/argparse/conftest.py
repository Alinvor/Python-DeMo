# -*- coding:utf-8 -*-

import os
import shutil
import tempfile
import pytest


@pytest.fixture(scope="session")
def _temp_dir():
    temp = tempfile.mkdtemp(prefix='argprase-')
    print('\n')
    print('the current temp dir is {}'.format(temp))
    yield temp
    shutil.rmtree(temp)


@pytest.fixture(scope="session")
def _temp_file():
    fd, temp = tempfile.mkstemp(prefix='argprase-', suffix='.tmp')
    # print('\n')
    print('the current temp path is {}'.format(temp))
    yield temp
    os.remove(temp)


# @pytest.mark.xfail(raises=ZeroDivisionError)
# def test_zero_division():
#     ''' test zero division'''
#     1/0
# with pytest.raises(ZeroDivisionError):
#     1 / 0
