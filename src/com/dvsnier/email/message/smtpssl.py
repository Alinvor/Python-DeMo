# -*- coding:utf-8 -*-

from com.dvsnier.email.message.smtp import Smtp

class SmtpSSL(Smtp, object):
    ''' the SMTP class that is use for send email '''

    def __init__(self):
        super(SmtpSSL, self).__init__()
