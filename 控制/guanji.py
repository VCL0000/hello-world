import smtplib
from email.mime.text import MIMEText


def guanji():
    sent = smtplib.SMTP('smtp.sina.com')
    sent.login('vcl0000@sina.com', 'C110eXZ110o')
    to = ['vcls032@sina.com']
    content = MIMEText('')
    content['Subject'] = 'guan'
    content['From'] = 'vcl0000@sina.com'
    content['To'] = ','.join(to)
    sent.sendmail('vcl0000@sina.com', to, content.as_string())
    sent.close()