# import os
import poplib  # 收邮件的
import smtplib  # 发邮件的
from email.header import decode_header  # 编码解码文件的
from email.mime.text import MIMEText  # 设置邮件内容
import email

# 登录邮箱
# 发送邮件登录和读取邮件登录

sent = smtplib.SMTP('smtp.sina.com')  # 邮箱的SMTP服务器地址
sent.login('vcls032@sina.com', 'VCL106514@o')
# 发送邮件
to = ['vcl0000@sina.com', 'vcls032@163.com']
content = MIMEText('hello,word')
content['Subject'] = "test"
content['From'] = 'vcls032@sina.com'
content['To'] = ','.join(to)
sent.sendmail('vcls032@sina.com', to, content.as_string())
sent.close()


# os.system('shutdown -s -t 60')
