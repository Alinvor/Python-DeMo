# -*- coding:utf-8 -*-


import smtplib
from com.dvsnier.email.message.mtp.smtp import Smtp


class SmtpSSL(Smtp, object):
    ''' the SMTP ssl class that is use for send email '''

    def __init__(self):
        super(SmtpSSL, self).__init__()
        self._smtpObj = smtplib.SMTP_SSL()

    def connect(self, host, port):
        super(SmtpSSL, self).connect(host, port)

    def login(self, user, password):
        super(SmtpSSL, self).login(user, password)

    def sendmail(self, from_addr, to_addrs, msg):
        super(SmtpSSL, self).sendmail(from_addr, to_addrs, msg)

    def quit(self):
        super(SmtpSSL, self).quit()
