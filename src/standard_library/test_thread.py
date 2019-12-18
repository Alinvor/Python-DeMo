# -*- coding: UTF-8 -*-

import thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))


if __name__ == "__main__":
    '''主函数入口'''
    # 创建两个线程
    try:
        thread.start_new_thread(print_time, (
            "Thread-1",
            2,
        ))
        thread.start_new_thread(print_time, (
            "Thread-2",
            4,
        ))
    except Exception as e:
        print "Error: unable to start thread"
    else:
        print "主程序-正常执行."

    time.sleep(27)
