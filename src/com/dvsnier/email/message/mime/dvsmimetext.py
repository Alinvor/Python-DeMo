# -*- coding:utf-8 -*-

from email.mime.text import MIMEText
from com.dvsnier.email.message.mime.dvsmimebase import DvsMIMEBase


class DvsMIMEText(DvsMIMEBase, object):
    ''' the MIME text class '''

    def __init__(self):
        super(DvsMIMEText, self).__init__()

    def execute(self):
        self._message = MIMEText()
        pass
