#coding=utf-8
from bs4 import BeautifulSoup
import requests

def get_html(url):
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ''(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=HEADERS)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    return None

def get_info(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup.find_all(attrs={'class': 'postbody'})

if __name__ == '__main__':
    url = "http://www.dxy.cn/bbs/thread/626626#626626"
    html = get_html(url)
    infos = get_info(html)
    for i in range(len(infos)):
        print('-'*100)
        print(infos[i].text.strip())    #利用strip()将获取的文本前后的空格删去，只留下文本
