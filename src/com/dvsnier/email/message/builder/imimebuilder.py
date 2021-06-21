# -*- coding:utf-8 -*-

from typing import Optional

from com.dvsnier.email.message.builder.ibuilder import IBuilder
from com.dvsnier.email.message.mtp.smtp import Smtp


class IMIMEBuilder(IBuilder, object):
    '''the mime build class'''

    # the smtp instance
    # _smtp = None
    _smtp: Optional[Smtp]

    def __init__(self, smtp):
        super(IMIMEBuilder, self).__init__()
        self._smtp = smtp

    def get_smtpObj(self):
        ''' the get smtp instance '''
        return self._smtpObj

    def set_smtpObj(self, smtpObj):
        ''' the set smtp instance '''
        if not smtpObj:
            raise KeyError('the smtp instance is undefined or invalid')
        self._smtpObj = smtpObj
        return self
