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
        current_branch = None
        current_branch_list_str = execute(["git branch"])
        if len(current_branch_list_str) > 0:
            branch_name_list = ' '.join(str(current_branch_list_str).split())
            if len(branch_name_list) > 0:
                branch_s = branch_name_list.split(' ')
                for index in range(len(branch_s)):
                    if branch_s[index] == '*':
                        current_branch = branch_s[index + 1]
                        break
            else:
                logging.warn('the current branch name list with re is vaild.')
            pass
        else:
            logging.warn('the current branch name is empty.')
        return current_branch

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
        return execute(['git branch -u origin/{0} {0}'.format(branch_name)])

    def get_current_branch_name(self):
        ''' the obtain current branch name '''
        return self._current_branch_name

    def set_current_branch_name(self, branch_name):
        ''' the set current branch name '''
        if not branch_name or not len(branch_name.strip()) > 0:
            logging.exception('the current branch name is invalid.')
            raise KeyError('the current branch name is invalid.')
        self._current_branch_name = branch_name

    def get_current_branch_list(self):
        'the current branch list'
        branch_queue = []
        branch_list_strs = execute(['git branch --list']).strip()
        if branch_list_strs:
            branch_list = branch_list_strs.split('\n')
            if branch_list:
                for branch in branch_list:
                    branch_element = branch.split(' ')
                    if branch_element:
                        branch_queue.append(branch_element[-1])
        return branch_queue

    def get_remote_branch_list(self):
        'the current remote branch list'
        branch_queue = []
        branch_list_strs = execute(['git branch --remotes']).strip()
        if branch_list_strs:
            branch_list = branch_list_strs.split('\n')
            if branch_list:
                for branch in branch_list:
                    branch_element = branch.split(' ')
                    if branch_element:
                        branch_queue.append(branch_element[-1])
        return branch_queue

    def get_remote_prune(self):
        'the remote prune'
        prune_result = execute(['git remote prune origin'])
        return prune_result

    def has_remote(self):
        'the judge whether the current git repository is associated with the remote repository'
        local_result = execute(['git config --local --list'])
        if local_result and local_result.find('remote.origin.url') >= 0 and local_result.find(
                'remote.origin.fetch') >= 0:
            return True
        return False

    def has_specifical_branch(self, branch_name, is_remote=False):
        'the judge whether the current git repository is specifical branch name'
        branch_list = []
        if is_remote:
            branch_list = self.get_remote_branch_list()
            if branch_name:
                branch_name = 'origin/' + branch_name
            else:
                raise KeyError('the current branch name is an invalid parameter value')
        else:
            branch_list = self.get_current_branch_list()
        if branch_name and branch_list and len(branch_list) > 0 and branch_name in branch_list:
            return True
        return False
