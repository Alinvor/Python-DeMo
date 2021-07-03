# -*- coding:utf-8 -*-

import logging
import os

from com.dvsnier.config.iconf import IConf


class Configuration(IConf, object):
    '''the Configuration class'''

    _config = {}

    def __init__(self):
        super(Configuration, self).__init__()

    def obtain_config(self, config_file):
        """the read xxx.cfg"""
        if not config_file or not os.path.exists(config_file):
            raise FileNotFoundError('the current config path is not found.')
        logging.info('the start parsing the configuration file that is {}'.format(os.path.abspath(config_file)))
        with open(config_file) as file_handler:
            lines = file_handler.readlines()
        for line in lines:
            if line.strip().startswith('#'):
                continue  # ignore notes
            else:
                try:
                    split_at = line.index("=")
                except ValueError:
                    continue  # ignore bad/empty lines
                else:
                    self._config[line[:split_at].strip()] = line[split_at + 1:].strip()
        return self._config


if __name__ == "__main__":
    '''主函数入口'''
    pass
