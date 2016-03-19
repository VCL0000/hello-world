import poplib  # 收邮件的
import smtplib  # 发邮件的
from email.header import decode_header  # 编码解码文件的
from email.mime.text import MIMEText  # 设置邮件内容
import email
import os
read = poplib.POP3('pop.sina.com')
read.user('vcl0000@sina.com')
read.pass_('C110eXZ110o')
tongji = read.stat()
str = read.top(tongji[0],0)
str2 = []
for x in str[1]:
    try:
        str2.append(x.decode())
    except:
        try:
            str2.append(x.decode('gnk'))
        except:
            str2.append(x.decode('gib5'))

msg = email.message_from_string('\n'.join(str2))
biaoti = decode_header(msg['subject'])
if biaoti[0][1]:
    biaoti2 = biaoti[0][0].decode(biaoti[0][1])
else:
    biaoti2= biaoti[0][0]

print(biaoti2)


if __name__=='__mian__':
    if biaoti2 == 'guan':
        os.system('shutdown -s -t 1')

    if biaoti2 =="xiu":
        os.system('shutdown -h')