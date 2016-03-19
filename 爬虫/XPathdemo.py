from lxml import etree

url = "http://www.meitulu.com/item/2998.html"
selector = etree.HTML(url)
content = selector.xpath('/html/body/div[3]/center[1]/img')
for each in content:
    print(each)
