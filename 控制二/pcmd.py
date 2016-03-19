import os
import time
while True:
    f = open('conf.ini','r')
    content = f.read()
    os.system(content)
    time.sleep(5)