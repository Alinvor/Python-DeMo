# -*- coding:utf-8 -*-


from com.dvsnier.email.config.config import Config


class Email(object):
    '''the email class'''

    # the config object
    _config = None

    def __init__(self):
        super(Email, self).__init__()
        self._config = Config()

    def template(self):
        ''' the template method '''
        pass

    def get_config(self):
        ''' the get config information '''
        return self._config

    # def set_config(self, config):
    #     ''' the set config information '''
    #     if not config:
    #         self._config = config

    def config_file(self, config_file):
        ''' the read xxx.cfg '''
        # logging.debug('the current config file is {}'.format(config_file))
        self._config.obtain_config(config_file)
        return self

    def get_config_info(self):
        ''' the get config information that dict typing '''
        return self.get_config().get_config()

    def init(self):
        ''' the initlizated email environment '''
        pass
