# -- coding:utf-8 --

import os
import subprocess


def test_popen(cmds):
    pin = subprocess.Popen(cmds[0], stdout=subprocess.PIPE, shell=True)
    print 'the current sub process pid(cwd: %s, ppid: %s, id: %s%d).' % (
        pin.pid, os.getppid(), type(pin), id(pin))
    processes = [pin]
    for x in cmds[1:]:
        # 管道流的输入应该是上个管道流的输出
        pout = subprocess.Popen(x,
                                stdin=pin.stdout,
                                stdout=subprocess.PIPE,
                                shell=True)
        print 'the current sub process pid(cwd: %s, ppid: %s, id: %s%d).' % (
            pout.pid, os.getppid(), type(pout), id(pout))
        # print type(pout), id(pout)
        processes.append(pout)
    print 'the current run process pid(cwd: %s, ppid: %s, id: %s%d).' % (
        pout.pid, os.getppid(), type(pout), id(pout))
    print type(pout), id(pout)
    output = pout.communicate()[0]
    # for p in processes:
    #     print 'the current wait pid(%s).' % p.pid
    #     p.wait()

    # print 'the current run process pid(cwd: %s, ppid: %s).' % (pout.pid,
    #                                                            os.getppid())
    content = output.rstrip('\n')
    print 'the current run process pid(cwd: %s, ppid: %s, id: %s%d).' % (
        pout.pid, os.getppid(), type(pout), id(pout))
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
    print result
