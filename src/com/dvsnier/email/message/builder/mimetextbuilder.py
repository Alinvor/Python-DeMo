# -*- coding:utf-8 -*-

from typing import Optional
from com.dvsnier.email.message.builder.abstractmimebuilder import AbstractMIMEBuilder
from com.dvsnier.email.message.mime.dvsmimetext import DvsMIMEText


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
        # 1. build mime object
        self._dvsMime = DvsMIMEText()
        # 2. the transmit what config object
        self._dvsMime.get_attribute().onConfig(self.get_config())
        # 3. set content
        self._dvsMime.get_attribute().set_content(self._content)
        # 4. set subtype that default plain type
        self._dvsMime.get_attribute().set_subtype('plain')
        # 5. set charset
        self._dvsMime.get_attribute().set_charset('utf-8')
        # 6. the execute function what is callback
        self._dvsMime.callback()
        # 7. the configure mime object
        self._smtp.set_mimeObj(self._dvsMime.get_message())
