#!/usr/bin/env python

# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# def get_xici_ip_from_api(None):
#         start_url='http://api.xicidaili.com/free2016.txt'
#         headers={
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari'
#         }
#         r=requests.get(start_url,headers=headers)
#         f=open('result/xici.txt','w')
#         f.write(r.text)
#         f.close()

def get_xici_ip_from_webpages(ip_type):
        start_url='http://www.xicidaili.com/'+str(ip_type)+'/'
        headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari'
        }
        r=requests.get(start_url,headers=headers)
        bs=BeautifulSoup(r.text,'lxml')
        datas=bs.find_all('br')
        # print datas
        # data=bs.select('#ip_list > tbody > tr:nth-child(2) > td')
        for data in datas:
                print data


get_xici_ip_from_webpages('nn')