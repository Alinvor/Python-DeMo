# -*- coding:utf-8 -*-

import os
import pytest


@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    ''' modarg '''
    param = request.param
    print("\n  SETUP modarg %s" % param)
    yield param
    print("\n  TEARDOWN modarg %s" % param)


@pytest.fixture(scope="function", params=[1, 2], ids=["func1", "func2"])
def funarg(request):
    ''' funarg '''
    param = request.param
    print("\n  SETUP funarg %s" % param)
    yield param
    print("\n  TEARDOWN funarg %s" % param)


def test_0(funarg):
    ''' test_0 '''
    print('  test scope: function')
    print("  RUN test0 with funarg %s" % funarg)


def test_1(modarg):
    ''' test_1 '''
    print('  test scope: module')
    print("  RUN test1 with modarg %s" % modarg)


def test_2(funarg, modarg):
    ''' test_2 '''
    print('  test scope: function and module')
    print("  RUN test2 with funarg %s and modarg %s" % (funarg, modarg))


if __name__ == "__main__":
    ''' the main point '''
    # function_argparse()
    retcode = pytest.main(args=['-v', '-s', os.path.abspath(__file__)])
    #
    # test function scope
    # retcode = pytest.main(args=['-v', '-s', '{}::{}'.format(os.path.abspath(__file__), 'test_0')])
    # test module scope
    # retcode = pytest.main(args=['-v', '-s', '{}::{}'.format(os.path.abspath(__file__), 'test_1')])
    # test scope with union function and module
    # retcode = pytest.main(args=['-v', '-s', '{}::{}'.format(os.path.abspath(__file__), 'test_2')])
    #
    # retcode = pytest.main(args=['--fixtures', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--collect-only', os.path.abspath(__file__)])
    print(retcode)
