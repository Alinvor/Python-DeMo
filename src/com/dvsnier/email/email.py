# -*- coding:utf-8 -*-

from com.dvsnier.email.config.config import Config
from com.dvsnier.email.message.builder.mimetextbuilder import MIMETextBuilder
from com.dvsnier.email.message.mtp.smtp import Smtp
from com.dvsnier.email.message.mtp.smtpssl import SmtpSSL


class Email(object):
    '''the email class'''

    # the config object
    # type: Union[Config]
    _config = None
    # the Smtp object
    # type: Union[SmtpBase]
    _smtp = None

    def __init__(self):
        '''
            the type comment reference:
                1. https://www.python.org/dev/peps/pep-0484/#suggested-syntax-for-python-2-7-and-straddling-code

            type: () -> None
        '''
        super(Email, self).__init__()
        self._config = Config()

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

    def init(self, mode=False):
        '''
            the initlizated email environment
            mode: true that is ssl mode, otherwise no
        '''
        if mode:
            self._smtp = SmtpSSL()
        else:
            self._smtp = Smtp()
        self._smtp.connect(self.get_config().get_mail_host(), self.get_config().get_mail_port())
        self._smtp.login(self.get_config().get_mail_user(), self.get_config().get_mail_pass())
        return self

    def builderText(self, content):
        ''' the default build content that is what subtype is plain and charset is utf-8 '''
        builder = MIMETextBuilder(self._smtp)
        builder.set_config(self.get_config())
        builder.setContent(content).build()

    def sendmail(self):
        ''' the send mail '''
        self._smtp.sendmail(self.get_config().get_mail_sender(), self.get_config().get_mail_receiver(),
        self._smtp.get_mimeObj().as_string())
        return self

    def quit(self):
        ''' the send mail '''
        self._smtp.quit()
