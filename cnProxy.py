#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import requests
from bs4 import BeautifulSoup
from userAgents import header
from proxiesList import proxy

# start_url='http://www.baidu.com'
start_url='http://cn-proxy.com/'
r=requests.get(start_url,headers=header,proxies=proxy)
time.sleep(2)
if r.status_code!=200:
    print '请求网页错误，请检查~'
    pass
else:
    print 'status_code=={}'.format(r.status_code)+',请求成功！'
    bs=BeautifulSoup(r.text,'lxml')
    print header
    print proxy
    print bs
