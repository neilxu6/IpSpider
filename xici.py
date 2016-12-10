# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import urllib2
import requests
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
def get_xici_ip_from_webpages(ip_type):
        countNum = 0
        start_url='http://www.xicidaili.com/'+str(ip_type)+'/'
        headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"}
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
                        protocol = str(tds[5].text.strip())
                        ip=str(tds[1].text.strip())
                        port = str(tds[2].text.strip())
                        # local = str(tds[3].text.strip())
                        # speed = str(tds[7].find('div')['title'].strip())
                        # time = str(tds[9].text.strip())
                        countNum += 1
                        print ('http://'+ip+':'+port)
                        if str(ip_type) in 'nn' or 'nt':
                                if str(protocol)=='HTTP':
                                        f0.write(ip + ':' + port + '\n')
                                        f1.write(ip+':'+port+'\n')
                                else:
                                        f0.write(ip + ':' + port + '\n')
                                        f2.write(protocol.lower()+'://'+ip+':'+port+'\n')
                        elif str(ip_type) in 'wn' or 'wt':
                                if str(protocol) == 'HTTP':
                                        f0.write(ip + ':' + port + '\n')
                                        f3.write(ip + ':' + port + '\n')
                                else:
                                        f0.write(ip + ':' + port + '\n')
                                        f4.write(protocol.lower() + '://' + ip + ':' + port + '\n')
                        else:
                                pass
        print '共'+str(countNum)+'个ip'
        return countNum



if __name__ == '__main__':
        f0=open('results/xici_results/xici.txt','a')
        f1=open('results/xici_results/xici_http_china.txt', 'a')
        f2=open('results/xici_results/xici_other_protocols_china.txt','a')
        f3=open('results/xici_results/xici_http_aborad.txt','a')
        f4=open('results/xici_results/xici_other_protocols_aborad.txt','a')
        f5=open('results/xici_results/xici_api.txt','a')

        get_xici_ip_from_webpages('nn')

        # get_xici_ip_from_api()

        f0.close()
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()