# -- coding:utf-8 --


import sys


def test_argv():
    argv = sys.argv[1:]
    # 输出格式:
    # ['start_date=2019', 'end_date=2020']
    # argv = sys.argv[:]
    # 输出格式:
    # ['test_argv.py', 'start_date=2019', 'end_date=2020']
    print(argv)


if __name__ == "__main__":
    '''主函数入口'''
    # the python command
    # python test_argv.py start_date=2019 end_date=2020
    test_argv()
