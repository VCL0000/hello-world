# get 发送数据
# post将数据放在header提交数据

    #network    点击加载下一页
    #Form Data
    #   entities_only: true
    #   page: 2
    #将这个数据做成一个字典    data
    #requests.post(url, data=data)  发送数据
    #正则匹配

import requests
import re

url = "https://www.crowdfunder.com"

data = {
    'entities_only': 'true',
    'page': '2'
}

html_post = requests.post(url, data=data)
reg = '"card-title">(.*?)</div>'
title = re.findall(reg, html_post.text, re.S)
for each in title:
    print(each)




