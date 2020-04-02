# -*- coding:utf-8 -*-

import os

# the define global cwd variable
cwd = os.getcwd()


def test_os_path():
    ''' the test os path '''
    absPath = os.path.abspath(cwd)
    print('the current abs path is %s' % absPath)
    baseName = os.path.basename(cwd)
    print('the current base name is %s' % baseName)
    # os.path.commonprefix(cwd)
    dirName = os.path.dirname(cwd)
    print('the current dir name is %s' % dirName)
    exists = os.path.exists(cwd)
    print('the current directory or file is exists that is %s ' % exists)
    userProfile = os.path.expanduser("~")
    print('the current user profile that is %s ' % userProfile)
    supportUnicodeFileNames = os.path.supports_unicode_filenames
    print('the current weather support unicode file names that is %s ' %
          supportUnicodeFileNames)


if __name__ == "__main__":
    '''主函数入口'''
    test_os_path()
