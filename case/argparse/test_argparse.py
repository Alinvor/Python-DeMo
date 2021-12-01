# -*- coding:utf-8 -*-

import argparse
import os
import pytest


def test_cmd_1(execute):
    ''' the test cmd '''
    print('\ntest_cmd_1: {}'.format(execute))
    print('the test_cmd_1 ended.')
    # pytest -v -s ./case/argparse/test_argparse.py
    # pytest -v -s test_argparse.py
    pass


@pytest.fixture(scope='session', params=['a', 'b', pytest.param('c', marks=pytest.mark.skip)])
def execute(_temp_dir, _temp_file, request):
    ''' the execute '''
    value = request.param
    print('\nexecute: {}'.format(value))
    return value


def function_argparse():
    #
    # the command line srcipt:
    #
    #   python test_argparse.py --help
    #
    parser = argparse.ArgumentParser(description='这是一个基本描述信息。')

    # Add optional switches
    parser.add_argument('-v', action='store_true', dest='is_verbose', help='produce verbose output')
    parser.add_argument('-o',
                        action='store',
                        dest='output',
                        metavar='FILE',
                        help='direct output to FILE instead of stdout')
    parser.add_argument('-C',
                        action='store',
                        type=int,
                        dest='context',
                        metavar='NUM',
                        default=0,
                        help='display NUM lines of added context')

    # Allow any number of additional arguments.
    parser.add_argument(nargs='*', action='store', dest='inputs', help='input filenames (default is stdin)')

    args = parser.parse_args()
    print(args.__dict__)


if __name__ == "__main__":
    ''' the main point '''
    # function_argparse()
    retcode = pytest.main(args=['-v', '-s', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--fixtures', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--collect-only', os.path.abspath(__file__)])
    print(retcode)
