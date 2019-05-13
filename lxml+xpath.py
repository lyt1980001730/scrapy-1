#coding=utf-8
from lxml import etree
import requests

#利用requests抓取网页
def get_html(url):
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ''(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=HEADERS)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    return None

#通过Xpath筛选出评论
def get_info(html):
    info_html = etree.HTML(html)
    result = info_html.xpath('//td[@class="postbody"]//text()')
    return result

#主体
if __name__ == '__main__':
    url = "http://www.dxy.cn/bbs/thread/626626#626626"
    html = get_html(url)
    infos = get_info(html)
    for i in range(len(infos)):
        print(infos[i].strip())
