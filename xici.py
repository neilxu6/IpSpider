#!/usr/bin/env python

# -*- coding: utf-8 -*-

import urllib2
import requests
from bs4 import BeautifulSoup

def get_xici_ip_from_api(None):
        start_url='http://api.xicidaili.com/free2016.txt'
        headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari'
        }
        r=requests.get(start_url,headers=headers)
        f=open('result/xici.txt','w')
        f.write(r.text)
        f.close()

def get_xici_ip_from_webpages(ip_type):
        countNum = 0
        proxyFile = open('proxy.txt', 'a')
        start_url='http://www.xicidaili.com/'+str(ip_type)+'/'

        requestHeader = {
                'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"}

        for page in range(1, 10):
                url = start_url + str(page)
                # print url
                request = urllib2.Request(url, headers=requestHeader)
                html_doc = urllib2.urlopen(request).read()

                soup = BeautifulSoup(html_doc, "html.parser")
                # print soup
                trs = soup.find('table', id='ip_list').find_all('tr')
                for tr in trs[1:]:
                        tds = tr.find_all('td')
                        # 国家
                        if tds[1].find('img') is None:
                                nation = '未知'
                                locate = '未知'
                        else:
                                nation = tds[1].find('img')['alt'].strip()
                                locate = tds[4].text.strip()
                        ip = tds[2].text.strip()
                        port = tds[3].text.strip()
                        anony = tds[5].text.strip()
                        protocol = tds[6].text.strip()
                        speed = tds[7].find('div')['title'].strip()
                        time = tds[9].text.strip()

                        proxyFile.write(
                                '%s|%s|%s|%s|%s|%s|%s|%s\n' % (nation, ip, port, locate, anony, protocol, speed, time))
                        # print '%s=%s:%s' % (protocol, ip, port)
                        countNum += 1
        proxyFile.close()
        return countNum

get_xici_ip_from_webpages('nn')