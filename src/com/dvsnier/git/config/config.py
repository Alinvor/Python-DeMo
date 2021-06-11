# -*- coding:utf-8 -*-

from com.dvsnier.git.git import Git
from com.dvsnier.process.execute import execute


class Config(Git, object):
    'the git config information'

    def __init__(self):
        super(Config, self).__init__()

    def global_info(self):
        'the global information'
        return execute(['git config --global --list'])

    def local_info(self):
        'the local git information'
        return execute(['git config --local --list'])
