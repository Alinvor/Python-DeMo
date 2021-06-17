# -*- coding:utf-8 -*-

from com.dvsnier.email.message.mime.iattribute import IAttribute


class IMIMEAttribute(IAttribute, object):
    ''' the MIME attribute class '''

    _sender = None
    _sender_alias = None
    _receiver = None
    _receiver_alias = None

    def __init__(self):
        super(IMIMEAttribute, self).__init__()

    def get_sender(self):
        ''' the get sender '''
        return self._sender

    def set_sender(self, sender):
        ''' the set sender '''
        self._sender = sender

    def get_sender_alias(self):
        ''' the get sender alias'''
        return self._sender_alias

    def set_sender_alias(self, sender_alias):
        ''' the set sender alias'''
        self._sender_alias = sender_alias

    def get_receiver(self):
        ''' the get receiver '''
        return self._receiver

    def set_receiver(self, receiver):
        ''' the set receiver '''
        self._receiver = receiver

    def get_receiver_alias(self):
        ''' the get receiver alias '''
        return self._receiver_alias

    def set_receiver_alias(self, receiver_alias):
        ''' the set receiver alias '''
        self._receiver_alias = receiver_alias


