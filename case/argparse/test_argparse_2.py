# -*- coding:utf-8 -*-

import argparse
import logging
import sys


def function_argparse():
    '''
        function_argparse

        reference link:

            1. https://docs.python.org/zh-cn/2.7/library/argparse.html
            2. https://docs.python.org/zh-cn/3.8/library/argparse.html

        usage: python -m build [-h] [--version] [--sdist] [--wheel] [--outdir OUTDIR] [--skip-dependency-check] [--no-isolation]
                       [--config-setting CONFIG_SETTING]
                       [srcdir]
    '''
    #
    # the command line srcipt:
    #
    #   python -m build -h
    #   python test_argparse_2.py --help
    #   python test_argparse_2.py -h
    #   python test_argparse_2.py ./a ./b
    #   python test_argparse_2.py ./a ./b -vs
    #   python test_argparse_2.py ./a ./b -v1 0
    #   python test_argparse_2.py ./a ./b -v1 1
    #   python test_argparse_2.py ./a ./b -v1 2
    #   python test_argparse_2.py ./a ./b -v2
    #   python test_argparse_2.py ./a ./b -v2 -v2
    #   python test_argparse_2.py ./a ./b -v
    #   python test_argparse_2.py ./a ./b -q
    #   python test_argparse_2.py ./a ./b -vs -v1 0
    #   python test_argparse_2.py ./a ./b -vs -v1 1
    #   python test_argparse_2.py ./a ./b -vs -v1 2
    #   python test_argparse_2.py ./a ./b -vs -v1 0 -v2
    #   python test_argparse_2.py ./a ./b -vs -v1 1 -v2
    #   python test_argparse_2.py ./a ./b -vs -v1 2 -v2
    #   python test_argparse_2.py ./a ./b -vs -v1 0 -v2 -v2
    #   python test_argparse_2.py ./a ./b -vs -v1 1 -v2 -v2
    #   python test_argparse_2.py ./a ./b -vs -v1 2 -v2 -v2
    #   python test_argparse_2.py ./a ./b -vs -v1 0 -v2 -v
    #   python test_argparse_2.py ./a ./b -vs -v1 1 -v2 -v
    #   python test_argparse_2.py ./a ./b -vs -v1 2 -v2 -v
    #   python test_argparse_2.py ./a ./b -vs -v1 0 -v2 -q
    #   python test_argparse_2.py ./a ./b -vs -v1 1 -v2 -q
    #   python test_argparse_2.py ./a ./b -vs -v1 2 -v2 -q
    #
    parser = argparse.ArgumentParser(description='这个是命令行总体多行文本描述信息.')
    # 位置参数
    parser.add_argument('srcdir', metavar='srcdir', type=str, help='这是一个 srcdir 位置参数')
    parser.add_argument('destdir', metavar='destdir', type=str, help='这是一个 destdir 位置参数')
    # 可选参数
    parser.add_argument('-vs', '--version', action="store_true", help='可选参数：显示版本号，并退出')
    parser.add_argument("-v1", "--verbosity_1", type=int, choices=[0, 1, 2], default=0, help="可选参数: 默认值形式")
    parser.add_argument("-v2", "--verbosity_2", action="count", default=0, help="可选参数: 默认值count 类型形式")
    # parser.add_argument('-l',
    #                     '--log',
    #                     default=sys.stdout,
    #                     type=argparse.FileType('w'),
    #                     help='the file where the sum should be written')
    # 可选参数，互斥选项
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", help='可选参数，互斥参数: the verbose info')
    group.add_argument("-q", "--quiet", action="store_true", help='可选参数，互斥参数: the quiet info')
    args = parser.parse_args()

    if args.srcdir:
        print('the args.srcdir: {}'.format(args.srcdir))
        logging.debug('the args.srcdir: {}'.format(args.srcdir))
    if args.destdir:
        print('the args.destdir: {}'.format(args.destdir))
        logging.debug('the args.destdir: {}'.format(args.destdir))
    if args.version:
        print('the args.version: {}'.format(args.version))
        logging.debug('the args.version: {}'.format(args.version))
    if args.verbosity_1 >= 0:
        print('the args.verbosity_1: {}'.format(args.verbosity_1))
        logging.debug('the args.verbosity_1: {}'.format(args.verbosity_1))
    if args.verbosity_2:
        print('the args.verbosity_2: {}'.format(args.verbosity_2))
        logging.debug('the args.verbosity_2: {}'.format(args.verbosity_2))
    if args.verbose:
        print('the args.verbose: {}'.format(args.verbose))
        logging.debug('the args.verbose: {}'.format(args.verbose))
    if args.quiet:
        print('the args.quiet: {}'.format(args.quiet))
        logging.debug('the args.quiet: {}'.format(args.quiet))
    # if args.log:
    #     args.log.write('%s' % sum(args.integers))
    #     args.log.close()


if __name__ == "__main__":
    ''' the main point '''
    function_argparse()
