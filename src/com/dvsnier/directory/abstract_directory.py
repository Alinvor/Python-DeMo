# -*- coding:utf-8 -*-

import logging
import os

from com.dvsnier.directory.idirectory import IDirectory


class AbstractDirectory(IDirectory, object):
    '''the Abstract Directory class'''
    # True: the strict mode, otherwise the base mode
    strategy_mode = False

    def __init__(self, strategy_mode=False):
        super(AbstractDirectory, self).__init__()
        self.strategy_mode = strategy_mode
        if self.strategy_mode:
            logging.warning(
                'At present, the strict review mode is adopted, and the illegal path is thrown directly. If the current directory is used by default to meet the current situation, please use the general review mode'
            )
        else:
            logging.debug(
                'Currently, the general review mode, workspace region space, current region space, executed region space and the same naming mode are used for the implementation of regional space'
            )

    def mk_dir(self, output_dir_name):
        'the initialize global output dir that two modes are provided, one is `strict mode`, the other is `general mode`, and the default is `general mode` (i.e. current work execution environment)'
        project_dir = None
        if self.strategy_mode:
            if self.get_work_region_space():
                project_dir = self.get_work_region_space()
            else:
                raise ValueError(
                    'In strict mode, illegal WORK_REGIOIN_SPACE value, please check WORK_REGIOIN_SPACE parameter.')
        else:
            project_dir = os.path.abspath('.')
        output_dir = os.path.join(project_dir, output_dir_name)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        return output_dir

    def mk_children_dir(self, output_dir_name, sub_dir_name):
        'the initialize children dir that default, the specified directory is created from the current execution environment'
        if not os.path.exists(output_dir_name):
            os.makedirs(output_dir_name)
        children_dir = os.path.join(output_dir_name, sub_dir_name)
        if not os.path.exists(children_dir):
            os.makedirs(children_dir)
        # logging.debug('the current children_dir is %s' % children_dir)
        return children_dir

    def mk_output_dir(self, output_dir_name, output_default_super_dir_name='out'):
        'the initialize output dir that two modes are provided, one is `strict mode`, the other is `general mode`, and the default is `general mode` (i.e. current work execution environment)'
        project_dir = None
        if self.strategy_mode:
            if self.get_work_region_space():
                project_dir = self.get_work_region_space()
            else:
                raise ValueError(
                    'In strict mode, illegal WORK_REGIOIN_SPACE value, please check WORK_REGIOIN_SPACE parameter.')
        else:
            project_dir = os.path.abspath('.')
        out_dir = os.path.join(project_dir, output_default_super_dir_name)
        output_dir = os.path.join(out_dir, output_dir_name)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        return output_dir
