# -*- coding:utf-8 -*-

from email.mime.text import MIMEText
from email.utils import formataddr
from com.dvsnier.email.message.mime.dvsmimebase import DvsMIMEBase
from com.dvsnier.email.message.mime.imimetextattribute import IMIMETextAttribute


class DvsMIMEText(DvsMIMEBase, object):
    ''' the MIME text class '''

    def __init__(self):
        super(DvsMIMEText, self).__init__()
        self._attribute = IMIMETextAttribute()

    def callback(self):
        super().callback()
        if not self.get_attribute():
            self._message = MIMEText(self.get_attribute().get_content(), self.get_attribute().get_subtype(),
            self.get_attribute().get_charset())
            self._message['Subject'] = self.get_subject()
            self._message['From'] = formataddr((self.get_attribute().get_sender_alias(),
            self.get_attribute().get_sender()), 'utf-8')
            self._message['To'] = formataddr((self.get_attribute().get_receiver_alias(),
            self.get_attribute().get_receiver()), 'utf-8')

