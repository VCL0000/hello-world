import time
import os
import poplib
import smtplib
from email.header import decode_header
from email.mime.text import MIMEText
import email

f = open('conf.ini', 'r')
w = f.read().split(',')
use = w[0]
pwd = w[1]
ser = w[2]
ser2 = w[3]
zdy = w[4]
zdyml = w[5]


def send():
    sent = smtplib.SMTP(ser)
    sent.login(use, pwd)
    to = [use]
    content = MIMEText('')
    content['Subject'] = 'reflash'
    content['From'] = use
    content['To'] = ','.join(to)
    sent.sendmail(use, to, content.as_string())
    sent.close()


def read():
    read = poplib.POP3(ser2)
    read.user(use)
    read.pass_(pwd)
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
    if biaoti2 == "chong":
        return 2
    if biaoti2 == zdy:
        return 3
    read.quit()


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
        if read() == 2:
            send()
            os.system('shutdown -r')
            break
        if read() == 3:
            send()
            os.system(zdyml)
            break
