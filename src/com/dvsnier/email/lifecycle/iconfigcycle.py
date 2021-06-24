# -*- coding:utf-8 -*-

from typing import Union
from com.dvsnier.email.config.config import Config
from com.dvsnier.email.lifecycle.icycle import ICycle


class IConfigCycle(ICycle, object):
    ''' the config cycle class '''

    # the config instance
    _config = None

    def __init__(self):
        super(IConfigCycle, self).__init__()

    def onConfig(self, config):
        ''' the configuration information execution mapping  '''
        # the maybe no required set config then you active to settings
        # self.set_config(config)
        pass

    def onExecute(self):
        ''' the dynamic code information execution mapping  '''
        pass

    def get_config(self):
        ''' the get config information '''
        return self._config

    def set_config(self, config):
        ''' the set config information '''
        self._config = config
        return self
