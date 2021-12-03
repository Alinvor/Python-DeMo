# -*- coding:utf-8 -*-

import os
import pytest


def test_parametrized_username_0(parametrized_username):
    ''' test_parametrized_username_0 '''
    assert parametrized_username in ['one', 'two', 'three']


def test_parametrized_username_1(non_parametrized_username):
    ''' test_parametrized_username_1 '''
    assert non_parametrized_username == 'username'


if __name__ == "__main__":
    ''' the main point '''
    retcode = pytest.main(args=['-v', '-s', os.path.abspath(__file__)])
    #
    # retcode = pytest.main(args=['-v', '-s', '{}::{}'.format(os.path.abspath(__file__), 'test_parametrized_username_0')])
    # retcode = pytest.main(args=['-v', '-s', '{}::{}'.format(os.path.abspath(__file__), 'test_parametrized_username_1')])
    #
    # retcode = pytest.main(args=['--fixtures', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--collect-only', os.path.abspath(__file__)])
    print(retcode)
