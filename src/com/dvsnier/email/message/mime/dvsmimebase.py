# -*- coding:utf-8 -*-

from com.dvsnier.email.message.mime.imimeattribute import IMIMEAttribute


class DvsMIMEBase(IMIMEAttribute, object):
    ''' the base MIME class '''

    _message = None

    def __init__(self):
        super(DvsMIMEBase, self).__init__()

    def get_message(self):
        ''' the get message '''
        return self._message

    def set_message(self, message):
        ''' the set message '''
        self._message = message
        return self
