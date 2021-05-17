# -*- coding:utf-8 -*-

from com.dvsnier.git.git import Git
from com.dvsnier.process.execute import execute


class Remote(Git, object):
    'the git remote command class'

    def __init__(self):
        super(Remote, self).__init__()

    def branch_prune(self):
        'the execute origin prune'
        return execute(['git remote prune origin'])
