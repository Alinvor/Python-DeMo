# -*- coding:utf-8 -*-

import logging
import threading
import time


def worker(arg):
    while not arg['stop']:
        logging.debug('我来自于工作线程...')
        time.sleep(5)


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(relativeCreated)6d %(threadName)s %(message)s')
    info = {'stop': False}
    thread = threading.Thread(target=worker, args=(info, ))
    thread.start()
    while True:
        try:
            logging.debug('我来自于主线程...')
            time.sleep(5)
        except KeyboardInterrupt:
            info['stop'] = True
            break
    thread.join()


if __name__ == "__main__":
    '''主函数入口'''
    main()
