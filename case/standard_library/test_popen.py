# -- coding:utf-8 --

import os
import subprocess


def test_popen(cmds):
    p = subprocess.Popen(cmds[0], stdout=subprocess.PIPE, shell=True)
    print 'the current sub process pid(cwd: %s, ppid: %s, id: %s%d).' % (
        p.pid, os.getppid(), type(p), id(p))
    processes = [p]
    for x in cmds[1:]:
        p = subprocess.Popen(x,
                             stdin=p.stdout,
                             stdout=subprocess.PIPE,
                             shell=True)
        print 'the current sub process pid(cwd: %s, ppid: %s, id: %s%d).' % (
            p.pid, os.getppid(), type(p), id(p))
        # print type(p), id(p)
        processes.append(p)
    print 'the current run process pid(cwd: %s, ppid: %s, id: %s%d).' % (
        p.pid, os.getppid(), type(p), id(p))
    print type(p), id(p)
    output = p.communicate()[0]
    # for p in processes:
    #     print 'the current wait pid(%s).' % p.pid
    #     p.wait()

    # print 'the current run process pid(cwd: %s, ppid: %s).' % (p.pid,
    #                                                            os.getppid())
    content = output.rstrip('\n')
    print 'the current run process pid(cwd: %s, ppid: %s, id: %s%d).' % (
        p.pid, os.getppid(), type(p), id(p))
    return content


if __name__ == "__main__":
    '''主函数入口'''
    print
    print 'the current run main process is (cwd: %s, ppid: %s).' % (
        os.getpid(), os.getppid())
    # git config --local --list | grep "user"
    # cmds = ["git config --local --list", "grep \"user\""]
    cmds = ["git config --local --list", "grep \"user\"", "grep \"@\""]
    result = test_popen(cmds)
    print 'the current run main process is (cwd: %s, ppid: %s).' % (
        os.getpid(), os.getppid())
    print 'the content is %s' % result
