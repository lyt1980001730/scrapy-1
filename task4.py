#coding=utf-8
import requests, json, re, random,time
from bs4 import BeautifulSoup
from selenium import webdriver
from lxml import etree


class getUrl(object):
    """docstring for getUrl"""
    def __init__(self):
        self.headers={
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8"
        };

    def run(self):
        browser = webdriver.Chrome()
        browser.get('https://auth.dxy.cn/login?service=http://www.dxy.cn/bbs/thread/626626')
        time.sleep(1)
        #切换账号密码登录表单
        js1 = 'document.querySelector("#j_loginTab1").style.display="none";'
        browser.execute_script(js1)
        time.sleep(1)
        js2 = 'document.querySelector("#j_loginTab2").style.display="block";'
        browser.execute_script(js2)
        #输入账号密码
        input_name = browser.find_element_by_name('username')
        input_name.clear()
        input_name.send_keys('******')
        input_pass = browser.find_element_by_name('password')
        input_pass.clear()
        input_pass.send_keys('******')
        browser.find_element_by_xpath('//*[@class="form__button"]/button').click()
        #此步骤应该有验证码，先跳过
        time.sleep(10)
        cookie = browser.get_cookies()
        cookie_dict = {i['name']:i['value'] for i in cookie}
        #转到抓取页面
        browser.get("http://www.dxy.cn/bbs/thread/626626#626626");
        html = browser.page_source
        tree = etree.HTML(html)
        user = tree.xpath('//div[@id="postcontainer"]//div[@class="auth"]/a/text()')
        content = tree.xpath('//td[@class="postbody"]')
        for i in range(0,len(user)):
            result = user[i].strip()+":"+content[i].xpath('string(.)').strip()
            #写入文件
            import io
            dir_file = io.open("DXY_records.txt",'a', encoding="utf-8")
            dir_file.write(result+"\n")
            strr='*' * 80 + "\n"
            strr=str.encode('utf-8')
            dir_file.write(strr)
            dir_file.close()
        print('*' * 5 +"抓取结束"+'*' * 5)


if __name__ == '__main__':
    geturl = getUrl()
    geturl.run()
