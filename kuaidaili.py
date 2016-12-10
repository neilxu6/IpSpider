#coding=utf-8
from bs4 import BeautifulSoup
import requests
import time
import random


# 每天获取ip和port的函数
def get_kuaidaili_ip_from_webpages(start_url,data=None):
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    }
    # 抓取快代理网站上的代理ip和port
    web_data=requests.get(start_url,headers=headers)
    time.sleep(6)
    soup=BeautifulSoup(web_data.text,'lxml')
    ips=soup.select('table > tbody > tr > td[data-title="IP"]')
    ports=soup.select('table > tbody > tr > td[data-title="PORT"]')
    for ip,port in zip(ips,ports):
        data='http://'+ip.get_text()+':'+port.get_text()+'/'
        f0.write(data+'\n')



if __name__ == '__main__':
        f0=open('results/kuaidaili_results/kuaidaili_http_china.txt', 'a')
        # f5=open('results/xici_results/xici_api.txt','a')

        for each_page_number in range(1, 11, 1):
            start_url = 'http://www.kuaidaili.com/proxylist/{}/'.format(str(each_page_number))
            # 调用函数
            get_kuaidaili_ip_from_webpages(start_url)
            print ('已完成第' + '#' + str(each_page_number) + '#' + '页的ip和port抓取~')
        print ('结束免费的ip和port抓取~')

        f0.close()
        # f5.close()


