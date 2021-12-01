# -*- coding:utf-8 -*-

import os
import pytest


@pytest.fixture(params=[0, 1, 2], ids=["spam", "ham", "asc"])
def a(request):
    ''' a '''
    return request.param


def test_a(a):
    ''' test_a '''
    pass


def idfn(fixture_value):
    ''' idfn '''
    if fixture_value == 0:
        return "eggs"
    else:
        return None


@pytest.fixture(params=[0, 1, 2], ids=idfn)
def b(request):
    ''' b '''
    return request.param


def test_b(b):
    ''' test_b '''
    pass


if __name__ == "__main__":
    ''' the main point '''
    retcode = pytest.main(args=['-v', '-s', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--fixtures', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--collect-only', os.path.abspath(__file__)])
    print(retcode)
