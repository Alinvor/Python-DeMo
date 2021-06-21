# -*- coding:utf-8 -*-

from typing import Optional, Union
from com.dvsnier.email.config.config import Config
from com.dvsnier.email.lifecycle.iconfigcycle import IConfigCycle
from com.dvsnier.email.message.builder.imimebuilder import IMIMEBuilder
from com.dvsnier.email.message.mime.imimeattribute import IMIMEAttribute
from com.dvsnier.email.message.mtp.smtpbase import SmtpBase


class AbstractMIMEBuilder(IMIMEBuilder, object):
    '''the mime build class'''

    # the config instance
    _config: Union[Config, None]

    def __init__(self, smtp):
        super(AbstractMIMEBuilder, self).__init__(smtp)

    def get_config(self):
        ''' the get config information '''
        return self._config

    def set_config(self, config):
        ''' the set config information '''
        self._config = config
