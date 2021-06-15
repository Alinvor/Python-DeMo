# -*- coding:utf-8 -*-

import logging
import os
import sys


class Config(object):
    '''the email config'''

    _sep = "\\" if sys.platform == "win32" else "/"  # no os module here yet - poor mans version

    def __init__(self):
        super(Config, self).__init__()

    def obtain_config(self, config_file):
        """the read xxx.cfg"""
        if not config_file or not os.path.exists(config_file):
            raise FileNotFoundError('the current config path is not found.')
        logging.debug('the current config file is {}'.format(os.path.abspath(config_file)))
        config = {}
        with open(config_file) as file_handler:
            lines = file_handler.readlines()
        for line in lines:
            try:
                split_at = line.index("=")
            except ValueError:
                continue  # ignore bad/empty lines
            else:
                config[line[:split_at].strip()] = line[split_at + 1:].strip()
        return config


