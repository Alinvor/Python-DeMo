# -*- coding:utf-8 -*-

import logging

from com.dvsnier.git.git import Git
from com.dvsnier.process.execute import execute


class Branch(Git, object):
    'the git branch command class'

    _current_branch_name = None

    def __init__(self):
        super(Branch, self).__init__()

    def get_branch(self):
        'the get current branch name'
        current_branch_list_str = execute(["git branch"])
        if len(current_branch_list_str) > 0:
            branch_name_list = ' '.join(str(current_branch_list_str).split())
            if len(branch_name_list) > 0:
                branch_s = branch_name_list.split(' ')
                for index in range(len(branch_s)):
                    if branch_s[index] == '*':
                        current_branch = branch_s[index + 1]
                        return current_branch
            else:
                logging.warn('the current branch name list with re is vaild.')
            pass
        else:
            logging.warn('the current branch name is empty.')

    def branch_to_file_and_commit_list(self):
        'the execute origin branch commit record list that to files'
        return execute([
            "git branch --list --all --sort=committerdate --format=\'%(color:reset)%(HEAD) %(color:yellow)%(refname:short)%(color:reset)|\
            %(color:red)%(objectname:short)\'"
        ])

    def branch_to_file_and_commit_list_with_more(self):
        '''the execute origin branch more commit record list that to files

            format one:
                git branch --list --all --sort=committerdate --format=\'%(HEAD) %(color:yellow)%(refname:short)%(color:reset)|
                %(color:red)%(objectname:short)%(color:reset)|%(color:reset)%(contents:subject)|%(authorname)|%(color:reset)(%(color:green)%(committerdate:relative)%(color:reset))\'

            format two:
                git branch --list --all --sort=committerdate --format=\'%(HEAD) %(color:yellow)%(refname:short)%(color:reset)|
                %(color:red)%(objectname:short)%(color:reset)|%(color:reset)(%(color:green)%(committerdate:relative)%(color:reset))\'
        '''
        return execute([
            "git branch --list --all --sort=committerdate --format=\'%(HEAD) %(color:yellow)%(refname:short)%(color:reset)|%(color:red)\
                %(objectname:short)%(color:reset)|%(color:reset)(%(color:green)%(committerdate:relative)%(color:reset))\'"
        ])

    def branch_set_upstream_to(self, branch_name):
        ''' the track remote and local branch associations '''
        if not branch_name or not len(branch_name.strip()) > 0:
            logging.exception('the current branch name is invalid.')
            raise KeyError('the current branch name is invalid.')
        return execute([
            'git branch -u origin/{0} {0}'.format(branch_name)
        ])

    def get_current_branch_name(self):
        ''' the obtain current branch name '''
        return self._current_branch_name

    def set_current_branch_name(self, branch_name):
        ''' the set current branch name '''
        if not branch_name or not len(branch_name.strip()) > 0:
            logging.exception('the current branch name is invalid.')
            raise KeyError('the current branch name is invalid.')
        self._current_branch_name = branch_name
