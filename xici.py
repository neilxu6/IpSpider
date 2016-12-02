#!/usr/bin/env python

# -*- coding: utf-8 -*-

import requests

def get_xici_ip(None):
        start_url='http://api.xicidaili.com/free2016.txt'
        headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari'
        }
        r=requests.get(start_url,headers=headers)
        f=open('result/xici.txt','w')
        f.write(r.text)
        f.close()

