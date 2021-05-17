# -*- coding:utf-8 -*-

from com.dvsnier.git.git import Git
from com.dvsnier.process.execute import execute
import logging


class Branch(Git, object):
    'the git branch command class'

    def __init__(self):
        super(Branch, self).__init__()

    def get_branch(self):
        'the get current branch name'
        current_branch_list_str = execute(["git branch"])
        if len(current_branch_list_str) > 0:
            branch_name_list = ' '.join(current_branch_list_str.split())
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
            'git branch --list --all --sort=committerdate --format=\'%(color:reset)%(HEAD) %(color:yellow)%(refname:short)%(color:reset)|%(color:red)%(objectname:short)\''
        ])

    def branch_to_file_and_commit_list_with_more(self):
        '''the execute origin branch more commit record list that to files

            format one:
                git branch --list --all --sort=committerdate --format=\'%(HEAD) %(color:yellow)%(refname:short)%(color:reset)|%(color:red)%(objectname:short)%(color:reset)|%(color:reset)%(contents:subject)|%(authorname)|%(color:reset)(%(color:green)%(committerdate:relative)%(color:reset))\'

            format two:
                git branch --list --all --sort=committerdate --format=\'%(HEAD) %(color:yellow)%(refname:short)%(color:reset)|%(color:red)%(objectname:short)%(color:reset)|%(color:reset)(%(color:green)%(committerdate:relative)%(color:reset))\'
        '''
        return execute([
            'git branch --list --all --sort=committerdate --format=\'%(HEAD) %(color:yellow)%(refname:short)%(color:reset)|%(color:red)%(objectname:short)%(color:reset)|%(color:reset)(%(color:green)%(committerdate:relative)%(color:reset))\''
        ])
