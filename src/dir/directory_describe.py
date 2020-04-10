# -*- coding:utf-8 -*-

import os
__cwd = None
__filter = []
__result = []


def get_current_directory():
    ''' the get current directory '''
    return __cwd


def set_current_directory(dir):
    ''' the set current directory '''
    global __cwd
    __cwd = dir


def get_current_filter():
    ''' the get current filter '''
    return __filter


def set_current_filter(filter=[]):
    ''' the set current filter '''
    global __filter
    __filter = filter


def get_current_result():
    ''' the get current result '''
    return __result


def clear():
    ''' the result list is clear '''
    global __result
    __result = []


def _query(dir_name):
    clear()
    for root, dirs, files in os.walk(dir_name):
        for fileName in files:
            absPath = os.path.join(root, fileName)
            get_current_result().append(absPath)
    return get_current_result()


def _queryAndFilter(dir_name, filter=[]):
    clear()
    for root, dirs, files in os.walk(dir_name):
        for fileName in files:
            absPath = os.path.join(root, fileName)
            ext = os.path.splitext(absPath)[1]
            if ext in filter:
                get_current_result().append(absPath)
    return get_current_result()


def execute():
    ''' the execute tasks '''
    absPath = os.path.abspath(get_current_directory())
    if (os.path.exists(absPath)):
        _query(absPath)


def executeFilter():
    ''' the execute tasks and filter '''
    absPath = os.path.abspath(get_current_directory())
    if (os.path.exists(absPath)):
        _query(absPath, get_current_filter())


if __name__ == "__main__":
    '''主函数入口'''
    # DeMo 实例
    absDir = '/Users/XXX/Documents/html'
    set_current_directory(absDir)
    execute()
    print('the current dir list is %s' % get_current_result())
