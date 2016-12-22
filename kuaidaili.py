#coding=utf-8
from bs4 import BeautifulSoup
import requests
import time


# 每天获取ip和port的函数
def kuaidaili_spider(start_url,data=None):
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    }
    web_data=requests.get(start_url,headers=headers)
    time.sleep(6)
    soup=BeautifulSoup(web_data.text,'lxml')
    ips=soup.select('table > tbody > tr > td[data-title="IP"]')
    ports=soup.select('table > tbody > tr > td[data-title="PORT"]')
    f1 = open('CN-IP.txt', 'r+a')
    for i in range(0,9):
        data=ips[i].get_text()+':'+ports[i].get_text()+'\n'
        f1.write(data)
    f1.close()

def run_kuaidaili_spider():

    for each_page_number in range(2, 4):
        start_url = 'http://www.kuaidaili.com/proxylist/{}/'.format(str(each_page_number))
        kuaidaili_spider(start_url)
        print ('已完成快代理网站第' + '#' + str(each_page_number) + '#' + '页的ip和port抓取~')
    print ('结束快代理网站的ip、port抓取任务！')

