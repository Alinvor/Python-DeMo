# -*- coding:utf-8 -*-

import argparse
import os
import subprocess
import pytest
import sys


def test_cmd_1(execute):
    ''' the test cmd '''
    print('the test_cmd_1 ended.')
    # pytest -v -s ./case/argparse/test_argparse_1.py
    # pytest -v -s test_argparse_1.py
    pass


@pytest.fixture()
def execute(_temp_dir, _temp_file):
    try:
        args = [sys.executable, __file__, '1']
        # args = [sys.executable, __file__, '-h']
        subprocess.check_output(args=args, )
        subprocess.check_call(args=args, )
    finally:
        print('the execute...')


def function_argparse():
    #
    # the command line srcipt:
    #
    #   python test_argparse_1.py --help
    #   python test_argparse_1.py 1
    #   python test_argparse_1.py 2
    #   python test_argparse_1.py 12 -l lasc.txt
    #   python test_argparse_1.py 12 --log asc.txt
    #
    parser = argparse.ArgumentParser(description='sum the integers at the command line')
    # 位置参数
    parser.add_argument('integers', metavar='int', nargs='+', type=int, help='an integer to be summed')
    # 可选参数
    parser.add_argument('-l',
                        '--log',
                        default=sys.stdout,
                        type=argparse.FileType('w'),
                        help='the file where the sum should be written')
    # parser.add_argument("-v", "--verbosity", action="count", default=0, help="increase output verbosity")
    # 可选参数，互斥选项
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", help='the verbose info')
    group.add_argument("-q", "--quiet", action="store_true", help='the quiet info')
    args = parser.parse_args()

    # if args.integers:
    #     args.integers = args.integers**2
    if args.log:
        args.log.write('%s' % sum(args.integers))
        args.log.close()


if __name__ == "__main__":
    ''' the main point '''
    function_argparse()
    # pytest.main(args=['-v', '-s', os.path.abspath(__file__)])
