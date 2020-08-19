# -- coding:utf-8 --

import getopt
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


def test_getopts():
    '''
    getopt函数的格式是getopt.getopt ( [命令行参数列表], "短选项", [长选项列表] )
    短选项名后的冒号(:)表示该选项必须有附加的参数。
    长选项名后的等号(=)表示该选项必须有附加的参数。
    '''
    short_opt = 'c:d'  # 短链选项
    long_args = ['info', 'debug', 'time=']  # 长链选项
    print
    sys_argv = sys.argv[1:]
    print 'the current sys_argv: %s' % sys_argv
    print
    opts, args = getopt.getopt(sys_argv, short_opt, long_args)
    print('the current opts type: %s' % type(opts))
    print('the current opts = %s' % opts)
    print ('the current opts[0] type: %s' % type(opts[0]))
    print
    print('the current args type: %s' % type(args))
    print ('the current args = %s' % args)
    print


def debug_print_command():
    '''
    命令输入,测试数据:
    1. python test_getopts.py -c c_args:c -d d start_date=2019 end_date=2020
    2. python test_getopts.py -c c_args:c -d start_date=2019 end_date=2020
    3. python test_getopts.py -c c_args:c -d --info start_date=2019 end_date=2020
    4. python test_getopts.py -c c_args:c -d --debug --time=the_current_system_time start_date=2019 end_date=2020
    '''
    argv = [
        'python', 'test_getopts.py', '-c', 'c_args:c', '-d', 'd', 'start_date=2019',
        'end_date=2020'
    ]
    print " ".join(argv)


if __name__ == "__main__":
    '''主函数入口'''
    test_getopts()
    # debug_print_command()
