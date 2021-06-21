# -*- coding:utf-8 -*-

from typing import Optional
from com.dvsnier.email.message.builder.abstractmimebuilder import AbstractMIMEBuilder


class MIMETextBuilder(AbstractMIMEBuilder, object):
    '''the mime build class'''

    _content: Optional[str]

    def __init__(self, smtp):
        super(MIMETextBuilder, self).__init__(smtp)

    # def onExecute(self):
    #     super().onExecute()
    #     if self.get_subtype():
    #         self.set_subtype('plain')
    #     if self.get_charset():
    #         self.set_charset('utf-8')

    def setContent(self, content):
        self._content = content
        return self

    def build(self):
        super().build()

        self._smtp.set_mimeObj(None)



