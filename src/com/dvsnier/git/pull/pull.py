# -*- coding:utf-8 -*-

from com.dvsnier.git.git import Git
from com.dvsnier.process.execute import execute


class Pull(Git, object):
    'the git pull command class'

    def __init__(self):
        super(Pull, self).__init__()

    def fast_foward(self):
        'the execute git pull origin option'
        return execute(['git pull --ff --stat origin'])
