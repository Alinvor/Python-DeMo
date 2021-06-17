# -*- coding:utf-8 -*-

import logging
import os
import sys


class Config(object):
    '''the email config'''

    _sep = "\\" if sys.platform == "win32" else "/"  # no os module here yet - poor mans version
    # the Set up server
    _mail_host = None
    # the Server SSL default port
    _mail_port = None
    # the email user name
    _mail_user = None
    # the email Password
    _mail_pass = None
    # the email Sender
    _mail_sender = None
    # the email Receiver
    _mail_receiver = None


    def __init__(self):
        super(Config, self).__init__()

    def obtain_config(self, config_file):
        """the read xxx.cfg"""
        if not config_file or not os.path.exists(config_file):
            raise FileNotFoundError('the current config path is not found.')
        logging.debug('the current config file is {}'.format(os.path.abspath(config_file)))
        config = {}
        with open(config_file) as file_handler:
            lines = file_handler.readlines()
        for line in lines:
            if line.strip().startswith('#'):
                continue # ignore notes
            else:
                try:
                    split_at = line.index("=")
                except ValueError:
                    continue  # ignore bad/empty lines
                else:
                    config[line[:split_at].strip()] = line[split_at + 1:].strip()
        logging.debug('the current config file: {}'.format(config))
        return config

    def get_mail_host(self):
        ''' the get mail host '''
        return self._mail_host

    def set_mail_host(self, mail_host):
        ''' the set mail host '''
        self._mail_host = mail_host
        return self

    def get_mail_port(self):
        ''' the get mail port '''
        return self._mail_port

    def set_mail_port(self, mail_port):
        ''' the set mail port '''
        self._mail_port = mail_port
        return self

    def get_mail_user(self):
        ''' the get mail user '''
        return self._mail_user

    def set_mail_user(self, mail_user):
        ''' the set mail user '''
        self._mail_user = mail_user
        return self

    def get_mail_pass(self):
        ''' the get mail password '''
        return self._mail_pass

    def set_mail_pass(self, mail_pass):
        ''' the set mail password '''
        self._mail_pass = mail_pass
        return self

    def get_mail_sender(self):
        ''' the get mail sender '''
        return self._mail_sender

    def set_mail_sender(self, mail_sender):
        ''' the set mail sender '''
        self._mail_sender = mail_sender
        return self

    def get_mail_receiver(self):
        ''' the get mail receiver '''
        return self._mail_receiver

    def set_mail_receiver(self, mail_receiver):
        ''' the set mail receiver '''
        self._mail_receiver = mail_receiver
        return self
