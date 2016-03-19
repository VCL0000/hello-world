import poplib
from email.header import decode_header
import email

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
    print(biaoti2)

    if biaoti2 == "guan":
        return 0
    if biaoti2 == "xiu":
        return 1
    read.quit()