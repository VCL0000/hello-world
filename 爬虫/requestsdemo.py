import re

import requests

# 获取网页源代码
#     网站有的网站会有反爬虫
# 在有反爬虫的
#   在审查元素-network中   随意点击内容
#   然后找到
#   User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36
#   这样的一个内容    创建一个User-Agent为键:后xx为值的字典 ZIDAINNAME ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36"}
#   在get(url,header=ZIDIANNAME)

# url = input("url:")
# url = "http://jp.tingroom.com/yuedu/yd300p/"
url = "http://tieba.baidu.com/p/4335857355?da_from=ZGFfbGluZT1EVCZkYV9wYWdlPTEmZGFfbG9jYXRlPXAwMDY0JmRhX2xvY19wYXJhbT0xJmRhX3Rhc2s9dGJkYSZkYV9vYmpfaWQ9MjY5MzEmZGFfb2JqX2dvb2RfaWQ9NDcwNzAmZGFfdGltZT0xNDU3NTcyNDgy&da_sign=f97e9979f30d6bba687d568e401045f1&tieba_from=tieba_da"
html = requests.get(url)

# 禁止爬虫依旧进行

hear = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36"}
# html = requests.get(url, headers=hear)
html.encoding = "utf-8"
print(html.text)

wbreg = '<span class="lzl_content_main">(.*?)</span>'
neirong = re.findall(wbreg, html.text, re.S)
for zz in neirong:
    print(zz)