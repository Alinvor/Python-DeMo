# -*- coding:utf-8 -*-

import logging

from com.dvsnier.config.journal.common_config import config
from deprecated import deprecated


@deprecated(version='0.0.2.dev1',
            reason="You should use the from com.dvsnier.config.common_config import config method, that We will delete \
this method after extending 2-3 versions")
def logging_conf(kwargs):
    '''
        the logging conf info:
            logging_conf(**kwargs={output_dir_name=\' \', file_name=\' \', level=logging.INFO})

        the level value range:
            - CRITICAL = 50
            - FATAL = CRITICAL
            - ERROR = 40
            - WARNING = 30
            - WARN = WARNING
            - INFO = 20
            - DEBUG = 10
            - NOTSET = 0
    '''
    if kwargs is not None and kwargs.get('level') is None:
        kwargs['level'] = logging.INFO
    return config(kwargs)
