# -- coding:utf-8 --

from multiprocessing import Lock, Pipe, Process, Queue
import os
import time


def info(title):
    ''' the print process information '''
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()


def fq(q):
    ''' the fq '''
    info('child')
    q.put('python-demo')
    q.put([42, None, 'hello'])


def fp(conn):
    ''' the fp '''
    info('child')
    conn.send('python-demo')
    conn.send([42, None, 'hello'])
    conn.close()


def flock(lock, i):
    ''' the flock '''
    lock.acquire()
    info('child')
    print 'hello world', i
    time.sleep(1)
    lock.release()


def test_queue():
    ''' 队列是线程和进程安全的 '''
    info('test_queue')
    q = Queue()
    p = Process(target=fq, args=(q, ))
    p.start()
    print q.get()
    p.join()


def test_pip():
    ''' Pipe() 函数返回一个由管道连接的连接对象，默认情况下是双工（双向） '''
    info('test_pip')
    parent_conn, child_conn = Pipe()
    p = Process(target=fp, args=(child_conn, ))
    p.start()
    print parent_conn.recv()
    p.join()


def test_lock():
    '''
        1. multiprocessing 包含来自 threading 的所有同步原语的等价物。
        2. 不使用来自不同进程的锁输出容易产生混淆。
    '''
    info('test_lock')
    lock = Lock()
    for num in range(10):
        Process(target=flock, args=(lock, num)).start()


if __name__ == "__main__":
    '''
        主函数入口
    '''
    # test_queue()
    # test_pip()
    test_lock()
