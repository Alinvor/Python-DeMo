# -*- coding:utf-8 -*-

import logging

from com.dvsnier.directory.common_dir import generate_complex_file_name


def config(kwargs):
    '''
        the logging config info:
            config(**kwargs={output_dir_name=\' \', file_name=\' \', level=logging.WARNING})

        the level value range:
            - CRITICAL = 50
            - FATAL = CRITICAL
            - ERROR = 40
            - WARNING = 30
            - WARN = WARNING
            - INFO = 20
            - DEBUG = 10
            - NOTSET = 0

        the article link reference:

            1. https://docs.python.org/zh-cn/2.7/howto/logging.html#logging-basic-tutorial
            2. https://docs.python.org/zh-cn/2.7/howto/logging.html#logging-advanced-tutorial
            3. https://docs.python.org/zh-cn/2.7/howto/logging-cookbook.html#logging-cookbook
            4. https://docs.python.org/zh-cn/2.7/library/logging.html
    '''
    if kwargs.get('output_dir_name') is None or len(kwargs.get('output_dir_name').strip()) == 0:
        raise KeyError('the current kwargs[output_dir_name] is empty.')
    if kwargs.get('file_name') is None or len(kwargs.get('file_name').strip()) == 0:
        raise KeyError('the current kwargs[file_name] is empty.')
    if kwargs.get('level') is not None and kwargs.get('level') < logging.NOTSET:
        raise KeyError('the current kwargs[level] is invalid.')
    elif kwargs.get('level') is None or kwargs.get('level') == logging.NOTSET:
        kwargs['level'] = logging.WARNING
    else:
        pass
    file_name = generate_complex_file_name(kwargs['output_dir_name'], kwargs['file_name'])
    logging.basicConfig(
        filename=file_name,
        filemode='a',
        format='[%(asctime)s][%(levelname)8s] --- %(message)s',
        # format=
        # '[%(asctime)s][%(levelname)8s][%(filename)s:%(lineno)s] --- %(message)s',
        level=kwargs['level'])
    logging.info('this current file is %s' % (file_name))
    return logging
