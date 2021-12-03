# -*- coding:utf-8 -*-

import os
import pytest


def test_username_0(username):
    ''' test_username_0 '''
    assert username == 'username'


@pytest.mark.parametrize('username', ['directly-overridden-username'])
def test_username_1(username):
    ''' test_username_1 '''
    assert username == 'directly-overridden-username'


@pytest.mark.parametrize('username', ['directly-overridden-username-other-repaired'])
def test_username_other(username, other_username):
    ''' test_username_other '''
    print('\n\n  test_username_other::username: {}'.format(username))
    print('  test_username_other::other_username: {}'.format(other_username))
    assert username == 'directly-overridden-username-other-repaired'
    assert other_username == 'other-directly-overridden-username-other-repaired'


@pytest.fixture
def parametrized_username():
    ''' parametrized_username '''
    return 'overridden-username'


@pytest.fixture(params=['one', 'two', 'three'])
def non_parametrized_username(request):
    ''' non_parametrized_username '''
    return request.param


def test_parametrized_username_0(parametrized_username):
    ''' test_parametrized_username_0 '''
    assert parametrized_username == 'overridden-username'


def test_parametrized_username_1(non_parametrized_username):
    ''' test_parametrized_username_1 '''
    assert non_parametrized_username in ['one', 'two', 'three']


if __name__ == "__main__":
    ''' the main point '''
    retcode = pytest.main(args=['-v', '-s', os.path.abspath(__file__)])
    #
    # retcode = pytest.main(args=['-v', '-s', '{}::{}'.format(os.path.abspath(__file__), 'test_username_0')])
    # retcode = pytest.main(args=['-v', '-s', '{}::{}'.format(os.path.abspath(__file__), 'test_username_1')])
    # retcode = pytest.main(args=['-v', '-s', '{}::{}'.format(os.path.abspath(__file__), 'test_username_other')])
    # retcode = pytest.main(args=['-v', '-s', '{}::{}'.format(os.path.abspath(__file__), 'test_parametrized_username_0')])
    # retcode = pytest.main(args=['-v', '-s', '{}::{}'.format(os.path.abspath(__file__), 'test_parametrized_username_1')])
    #
    # retcode = pytest.main(args=['--fixtures', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--collect-only', os.path.abspath(__file__)])
    print(retcode)
