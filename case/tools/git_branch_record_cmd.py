# -*- coding:utf-8 -*-

import logging
import os
from com.dvsnier.conf.common_conf import logging_conf
from com.dvsnier.process.execute import execute
from com.dvsnier.dir.common_dir import generate_fmt_file_name


def get_branch():
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


def fast_foward():
    'the execute git pull origin option'
    return execute(['git pull origin'])


def branch_checkout(branch):
    'the switch to destination branch'
    # execute(['git status'])
    execute(['git stash'])
    return execute(['git checkout {branch}'.format(branch=branch)])


def branch_prune():
    'the execute origin prune'
    return execute(['git remote prune origin'])


def branch_to_file_and_commit_list():
    'the execute origin branch commit record list that to files'
    return execute([
        'git branch --list --all --sort=committerdate --format=\'%(color:reset)%(HEAD) %(color:yellow)%(refname:short)%(color:reset)|%(color:red)%(objectname:short)\''
    ])


def branch_to_file_and_commit_list_with_more():
    '''the execute origin branch more commit record list that to files

        format one:
            git branch --list --all --sort=committerdate --format=\'%(HEAD) %(color:yellow)%(refname:short)%(color:reset)|%(color:red)%(objectname:short)%(color:reset)|%(color:reset)%(contents:subject)|%(authorname)|%(color:reset)(%(color:green)%(committerdate:relative)%(color:reset))\'

        format two:
            git branch --list --all --sort=committerdate --format=\'%(HEAD) %(color:yellow)%(refname:short)%(color:reset)|%(color:red)%(objectname:short)%(color:reset)|%(color:reset)(%(color:green)%(committerdate:relative)%(color:reset))\'
    '''
    return execute([
        'git branch --list --all --sort=committerdate --format=\'%(HEAD) %(color:yellow)%(refname:short)%(color:reset)|%(color:red)%(objectname:short)%(color:reset)|%(color:reset)(%(color:green)%(committerdate:relative)%(color:reset))\''
    ])


if __name__ == "__main__":
    '''Git 分支记录脚本'''
    # /Users/.../Python-DeMo
    engineering_dir = os.getcwd()
    #
    # 工程目录,请设置为将要统计的项目绝对路径
    #
    project_dir = ''  # 项目路径
    env = 'Test'  # Test Environment
    if project_dir is None or project_dir == '':
        raise ValueError('the current project_dir is empty.')
    kwargs = {'output_dir_name': 'git', 'file_name': 'branch'}
    logging_conf(kwargs)
    logging.debug('the current engineering_dir: {engineering_dir}'.format(
        engineering_dir=engineering_dir))
    logging.debug('the current project_dir: {project_dir}'.format(
        project_dir=project_dir))
    os.chdir(project_dir)
    current_branch_name = get_branch()
    logging.debug(
        'the current branch: {branch}'.format(branch=current_branch_name))
    if current_branch_name != env:
        branch_checkout(env)
    ff_result = fast_foward()
    logging.debug('the current branch status: {branch_status}'.format(
        branch_status=ff_result))
    branch_prune()
    value = branch_to_file_and_commit_list()
    # value = branch_to_file_and_commit_list_with_more()
    os.chdir(engineering_dir)
    with open(generate_fmt_file_name('resource', 'resource'), 'w+') as file:
        file.write(value)
    pass
