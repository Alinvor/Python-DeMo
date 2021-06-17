# -*- coding:utf-8 -*-

class Smtp(object):
    ''' the SMTP class that is use for send email '''

    # the smtp instance
    _smtpObj = None

    def __init__(self):
        super(Smtp, self).__init__()

    def get_smtpObj(self):
        ''' the get smtp instance '''
        return self._smtpObj

    def set_smtpObj(self, smtpObj):
        ''' the set smtp instance '''
        if not smtpObj:
            raise KeyError('the smtp instance is undefined or invalid')
        self._smtpObj = smtpObj
