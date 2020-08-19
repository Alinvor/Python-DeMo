# -*- coding: UTF-8 -*-

import thread
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_port = 465  # 服务器SSL 默认端口

mail_user = "xxx"  # 用户名
mail_pass = "xxx"  # 口令

sender = 'xxx'  # 发送人
receiver = 'xxx'  # 接收人


def obtainMailMessage():
    ''' 邮件配置信息 '''
    # 三个参数：
    #   第一个为文本内容;
    #   第二个 plain 设置文本格式;
    #   第三个 utf-8 设置编码;
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    message['From'] = formataddr(['资深好男人', sender])
    # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    message['To'] = formataddr(['我可姿势江山美如画', receiver])
    # 邮件的主题，也可以说是标题
    message['Subject'] = 'Python SMTP SSL 邮件测试'
    return message


def sendMail():
    ''' 发送邮件 '''
    smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
    smtpObj.login(mail_user, mail_pass)
    content = obtainMailMessage().as_string()
    print
    print content
    smtpObj.sendmail(sender, [
        receiver,
    ], content)
    smtpObj.quit()


if __name__ == "__main__":
    '''主函数入口'''
    try:
        thread.start_new_thread(sendMail, ())
        time.sleep(5)
        print "邮件发送成功"
    except Exception as e:
        # print e.message
        print "Error: 无法发送邮件"
