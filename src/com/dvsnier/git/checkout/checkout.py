# -*- coding:utf-8 -*-

from com.dvsnier.git.git import Git
from com.dvsnier.process.execute import execute


class Checkout(Git, object):
    'the git checkout command class'

    def __init__(self):
        super(Checkout, self).__init__()

    def branch_checkout(self, branch):
        'the switch to destination branch'
        if branch is None or len(branch) == 0:
            raise KeyError('the branch value is empty.')
        # execute(['git status'])
        execute(['git stash'])
        return execute(['git checkout {branch}'.format(branch=branch)])
