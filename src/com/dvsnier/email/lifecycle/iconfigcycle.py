# -*- coding:utf-8 -*-

from com.dvsnier.email.lifecycle.icycle import ICycle


class IConfigCycle(ICycle, object):
    ''' the config cycle class '''

    def __init__(self):
        super(IConfigCycle, self).__init__()

    def onConfig(self, config):
        ''' the configuration information execution mapping  '''
        pass

    def onExecute(self):
        ''' the dynamic code information execution mapping  '''
        pass
