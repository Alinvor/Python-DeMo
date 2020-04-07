# -*- coding:utf-8 -*-

import os
__cwd = None


def get_current_directory():
    ''' the get current directory '''
    return __cwd


def set_current_directory(dir):
    ''' the set current directory '''
    global __cwd
    __cwd = dir


def execute():
    ''' the execute tasks '''
    absPath = os.path.abspath(get_current_directory())
    if (os.path.exists(absPath)):
        recursion(absPath)


def recursion(dest):
    ''' the recursion file or directory '''
    if (os.path.isdir(dest)):
        os.listdir(dest)
        pass
    else:
        pass


if __name__ == "__main__":
    '''主函数入口'''
    pass
