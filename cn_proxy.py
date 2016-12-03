#coding=utf-8
from bs4 import BeautifulSoup
import requests
import time
import random
import pymongo

# client = pymongo.MongoClient('localhost', 27017)
# proxy = client['get_ip_and_port']
# ip_and_port_table = proxy['2016_11_17_before_check']

# 每天获取ip和port的函数
def spider1(start_url,data=None):
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    }
    proxy_list = [
        'http://1.82.216.134:80',
        'http://211.153.17.151:80',
    ]
    proxy_ip = random.choice(proxy_list)  # 随机获取代理ip
    proxies = {'http': proxy_ip}
    # ,proxies=proxies
    # 抓取快代理网站上的代理ip和port
    web_data=requests.get(start_url,headers=headers,proxies=proxies)
    time.sleep(1)
    soup=BeautifulSoup(web_data.text,'lxml')
    ips=soup.select('table > tbody > tr > td[data-title="IP"]')
    ports=soup.select('table > tbody > tr > td[data-title="PORT"]')
    for ip,port in zip(ips,ports):
        data={
            'ip':ip.get_text(),
            'port':port.get_text(),
        }
        # ip_and_port_table.insert(data)
        print ("插入一条成功")


for each_page_number in range(1,10,1):
    start_url = 'http://www.kuaidaili.com/proxylist/{}/'.format(str(each_page_number))
    # 调用函数
    spider1(start_url)
    print ('已完成第'+'#'+str(each_page_number)+'#'+'页的ip和port抓取~')
print ('结束免费的ip和port抓取~')




