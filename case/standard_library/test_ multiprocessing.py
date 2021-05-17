# -- coding:utf-8 --

from multiprocessing import Process
import os


def info(title):
    ''' the print process information '''
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()


def function(name):
    ''' the function '''
    info('function ')
    print 'hello', name


if __name__ == "__main__":
    '''主函数入口'''
    info('main')
    p = Process(target=function, args=('python-demo', ))
    p.start()
    p.join()
