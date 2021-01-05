# -*- coding:utf-8 -*-

import logging
import os
from com.dvsnier.conf.common_conf import Conf, logging_conf
from com.dvsnier.git.branch.branch import Branch
from com.dvsnier.git.checkout.checkout import Checkout
from com.dvsnier.git.pull.pull import Pull
from com.dvsnier.git.remote.remote import Remote
from com.dvsnier.dir.common_dir import generate_fmt_file_name


def execute(project_dir, env):
    # /Users/.../Python-DeMo
    engineering_dir = os.getcwd()
    if project_dir is None or project_dir == '':
        raise ValueError('the current project_dir is empty.')
    kwargs = {'output_dir_name': 'git', 'file_name': 'branch'}
    logging_conf(kwargs)
    logging.debug('the current engineering_dir: {engineering_dir}'.format(
        engineering_dir=engineering_dir))
    logging.debug('the current project_dir: {project_dir}'.format(
        project_dir=project_dir))
    os.chdir(project_dir)
    branch = Branch()
    checkout = Checkout()
    current_branch_name = branch.get_branch()
    logging.debug(
        'the current branch: {branch}'.format(branch=current_branch_name))
    if current_branch_name != env:
        checkout.branch_checkout(env)
    ff_result = Pull().fast_foward()
    logging.debug('the current branch status: {branch_status}'.format(
        branch_status=ff_result))
    Remote().branch_prune()
    value = branch.branch_to_file_and_commit_list()
    # value = branch.branch_to_file_and_commit_list_with_more()
    os.chdir(engineering_dir)
    with open(generate_fmt_file_name('resource', 'resource'), 'w+') as file:
        file.write(value)


if __name__ == "__main__":
    '''
        Git 分支记录脚本,目前只支持单进程模式
        目前需要配置如下:

            1. project_dir: 项目工程绝对路径
            2. env：项目工程分支名称，默认为Test 分支
        配置文件格式：

        [git_branch_record_cmd]
        project_dir = /Users/.../Python-DeMo  # 项目路径
        env = Test # Test Environment

    '''
    config = Conf()
    config.read(os.path.join('conf', 'git_config.cfg'))
    #
    # 工程目录,请设置为将要统计的项目绝对路径
    #
    project_dir = config.get('git_branch_record_cmd', 'project_dir')
    #
    # 工程分支，默认为Test 分支
    #
    env = config.get('git_branch_record_cmd', 'env')
    config.debug()
    execute(project_dir, env)
