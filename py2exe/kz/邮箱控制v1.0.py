import time
import os
import poplib
import smtplib
from email.header import decode_header
from email.mime.text import MIMEText
import email


def send():
    sent = smtplib.SMTP('smtp.sina.com')
    sent.login('vcl0000@sina.com', 'C110eXZ110o')
    to = ['vcls032@sina.com']
    content = MIMEText('')
    content['Subject'] = 'reflash'
    content['From'] = 'vcl0000@sina.com'
    content['To'] = ','.join(to)
    sent.sendmail('vcl0000@sina.com', to, content.as_string())
    sent.close()


def xiu():
    sent = smtplib.SMTP('smtp.sina.com')
    sent.login('vcl0000@sina.com', 'C110eXZ110o')
    to = ['vcls032@sina.com']
    content = MIMEText('')
    content['Subject'] = 'xiu'
    content['From'] = 'vcl0000@sina.com'
    content['To'] = ','.join(to)
    sent.sendmail('vcl0000@sina.com', to, content.as_string())
    sent.close()


def read():
    read = poplib.POP3('pop.sina.com')
    read.user('vcls032@sina.com')
    read.pass_('VCL106514@o')
    tongji = read.stat()
    str = read.top(tongji[0], 0)
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
        biaoti2 = biaoti[0][0]

    if biaoti2 == "guan":
        return 0
    if biaoti2 == "xiu":
        return 1
    read.quit()

# print(send())
if __name__ == '__main__':
    while True:
        time.sleep(2)
        if read() == 0:
            os.system('shutdown -s -t 10')
            send()
            break
        if read() == 1:
            send()
            os.system('shutdown -h')
            break
