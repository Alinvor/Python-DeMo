# -*- coding:utf-8 -*-

import logging


class IDirectory(object):
    '''the IDirectory class'''

    __WORK_REGIOIN_SPACE = None
    __CURRENT_REGION_SPACE = None
    __EXECUTED_REGION_SPACE = None

    def __init__(self):
        super(IDirectory, self).__init__()

    def get_work_region_space(self):
        'the get work region space'
        return self.__WORK_REGIOIN_SPACE

    def set_work_region_space(self, work_region_space):
        'the set work region space'
        self.__WORK_REGIOIN_SPACE = work_region_space
        return self

    def get_current_region_space(self):
        'the get current region space'
        if not self.__CURRENT_REGION_SPACE:
            self.__CURRENT_REGION_SPACE = self.__WORK_REGIOIN_SPACE
            logging.warning('the current region space is not initialized, and then the default value is used.')
        return self.__CURRENT_REGION_SPACE

    def set_current_region_space(self, current_region_space):
        'the set current region space'
        self.__CURRENT_REGION_SPACE = current_region_space
        return self

    def get_executed_region_space(self):
        'the get executed region space'
        if not self.__EXECUTED_REGION_SPACE:
            self.__EXECUTED_REGION_SPACE = self.__WORK_REGIOIN_SPACE
            logging.warning('the executed region space is not initialized, and then the default value is used.')
        return self.__EXECUTED_REGION_SPACE

    def set_executed_region_space(self, executed_region_space):
        'the set executed region space'
        self.__EXECUTED_REGION_SPACE = executed_region_space
        return self
