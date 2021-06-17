# -*- coding:utf-8 -*-

from com.dvsnier.email.message.mime.mimebase import MIMEBase
from com.dvsnier.email.message.mime.imimetextattribute import IMIMETextAttribute


class MIMEText(MIMEBase, IMIMETextAttribute, object):
    ''' the MIME text class '''

    def __init__(self):
        super(MIMEText, self).__init__()
