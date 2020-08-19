# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'dovsnier@qq.com'  # 发送人
receiver = ['zhenwei-li@qq.com']  # 接收人


def obtainMailMessage():
    '''邮件配置信息'''
    # 三个参数：
    #   第一个为文本内容;
    #   第二个 plain 设置文本格式;
    #   第三个 utf-8 设置编码;
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("资深好男人 From", 'utf-8')
    message['To'] = Header("我可姿势江山美如画 To", 'utf-8')
    message['Subject'] = Header('Python SMTP 邮件测试', 'utf-8')
    return message


if __name__ == "__main__":
    '''
        通过本地设备sendmail 库进行发送邮件

        启动命令:
        python -m smtpd -n -c DebuggingServer localhost:1025
    '''
    try:
        smtpObj = smtplib.SMTP('localhost', 1025)
        content = obtainMailMessage().as_string()
        print
        print content
        '''
            Content-Type: text/plain; charset="utf-8"
            MIME-Version: 1.0
            Content-Transfer-Encoding: base64
            From: =?utf-8?b?6LWE5rex5aW955S35Lq6IEZyb20=?=
            To: =?utf-8?b?5oiR5Y+v5ae/5Yq/5rGf5bGx576O5aaC55S7IFRv?=
            Subject: =?utf-8?b?UHl0aG9uIFNNVFAg6YKu5Lu25rWL6K+V?=

            UHl0aG9uIOmCruS7tuWPkemAgea1i+ivlS4uLg==
        '''
        smtpObj.sendmail(sender, receiver, content)
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"
