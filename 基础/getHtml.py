from urllib import request

def getHtml(url):
    page = request.urlopen(url)
    html = page.read()
    html = html.decode(encoding='UTF-8')
    return html


html = getHtml("http://www.baidu.com")
print(html)