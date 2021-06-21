# -*- coding:utf-8 -*-

from com.dvsnier.email.config.config import Config
from com.dvsnier.email.message.builder.imimebuilder import IMIMEBuilder
from com.dvsnier.email.message.mime.dvsmimebase import DvsMIMEBase


class AbstractMIMEBuilder(IMIMEBuilder, object):
    '''the mime build class'''

    # the config instance
    _config = None
    # the dvs mime instance
    _dvsMime = None

    def __init__(self, smtp):
        super(AbstractMIMEBuilder, self).__init__(smtp)

    def get_config(self):
        ''' the get config information '''
        return self._config

    def set_config(self, config):
        ''' the set config information '''
        self._config = config

    def get_dvsMime(self):
        ''' the get dvsMime information '''
        return self._dvsMime

    def set_dvsMime(self, dvsMime):
        ''' the set dvsMime information '''
        self._dvsMime = dvsMime