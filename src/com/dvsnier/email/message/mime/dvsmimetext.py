# -*- coding:utf-8 -*-

from email.mime.text import MIMEText
from com.dvsnier.email.message.mime.dvsmimebase import DvsMIMEBase
from com.dvsnier.email.message.mime.imimetextattribute import IMIMETextAttribute


class DvsMIMEText(DvsMIMEBase, IMIMETextAttribute, object):
    ''' the MIME text class '''

    def __init__(self):
        super(DvsMIMEText, self).__init__()
