# -*- coding:utf-8 -*-

from com.dvsnier.email.message.mime.imimeattribute import IMIMEAttribute


class MIMEBase(IMIMEAttribute, object):
    ''' the base MIME class '''

    def __init__(self):
        super(MIMEBase, self).__init__()

