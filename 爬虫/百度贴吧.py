# _*_conding:utf-8_*_
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json


# import sys
#
# reload(sys)
# sys.setdefauttencoding('utf-8')

def woerite(contentdict):
    f.writelines(u'回帖时间:' + str(contentdict['topic_reply_time']) + '\n')
    f.writelines(u'回帖内容:' + unicode(contentdict['topic_reply_content']) + '\n')
    f.writelines(u'回帖人:' + contentdict['user_name'] + '\n\n')


def spider(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    content_field = selector.xpath('//*[@id="j_p_postlist"]')
    item = {}
    for each in content_field:
        reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot', ''))
        author = reply_info['author']['user_name']
        content = \
            each.xpath(
                'div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content "]/text()')[0]
        reply_time = reply_info['content']['date']

        print(content)
        print(reply_time)
        print(author)
        item['user_name'] = author
        item['topic_reply_content'] = content
        item['topic_reply_time'] = reply_time


if __name__ == '__main__':
    pool = ThreadPool(2)
    f = open('content.txt', 'a')
    page = []
    for i in range(1, 21):
        newpage = 'http://tieba.baidu.com/p/3522395718?pn=' + str(i)
        page.append(newpage)

    rseults = pool.map(spider(), page)

    pool.close()
    pool.join()
    f.close()
