# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import urllib2
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



# 来源一：从api中获取ip
# def get_xici_ip_from_api():
#         start_url='http://api.xicidaili.com/free2016.txt'
#         headers={
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari'
#         }
#         r=requests.get(start_url,headers=headers)
#         f5.write('http://'+str(r.text))
#         print ('http://'+str(r.text))

# proxy="http://112.25.41.136:80"
# proxy_support=urllib.request.ProxyHandler({'http':proxy})
# opener = urllib.request.build_opener(proxy_support)
# urllib.request.install_opener(opener)
# r = urllib.request.urlopen('http://icanhazip.com',timeout = 1000)


# 来源二：从网页上爬取ip
def xici_spider(ip_type):
        countNum = 0
        start_url='http://www.xicidaili.com/'+str(ip_type)+'/'
        headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"}
        f1 = open('CN-IP.txt', 'r+a')
        for page in range(1, 10):
                url = start_url + str(page)
                # 这个网站对请求次数很敏感，可能网站规模不大大家手下留情
                time.sleep(10)
                request = urllib2.Request(url, headers=headers)
                html_doc = urllib2.urlopen(request).read()
                soup = BeautifulSoup(html_doc, "html.parser")
                trs = soup.find('table', id='ip_list').find_all('tr')
                for tr in trs[1:]:
                        tds = tr.find_all('td')
                        # protocol = str(tds[5].text.strip())
                        ip=str(tds[1].text.strip())
                        port = str(tds[2].text.strip())
                        # local = str(tds[3].text.strip())
                        # speed = str(tds[7].find('div')['title'].strip())
                        # time = str(tds[9].text.strip())
                        countNum += 1
                        f1.write(ip+':'+port+'\n')
                print '已完成西刺网站第'+str(page)+'页的IP信息爬取~'
        f1.close()
        print '西刺网站已全部爬取完毕！'



def run_xici_spider():
        xici_spider('nn')
        time.sleep(16)
        xici_spider('nt')
        time.sleep(16)
        xici_spider('wt')

