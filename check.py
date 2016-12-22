#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import httplib



def check_task():
    inFile = open('CN-IP.txt', 'r+a')
    outFile = open('verified.txt', 'r+a')
    target_url='http://www.baidu.com'
    headers ={
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"
        }
    while True:
        ll = inFile.readline().strip()
        if len(ll) == 0: break
        line = ll.strip().split(':')
        ip = line[0]
        port = line[1]
        try:
            conn = httplib.HTTPConnection(ip, port, timeout=5.0)
            time.sleep(1)
            conn.request(method='GET', url=target_url, headers=headers)
            res = conn.getresponse()
            print "+++Success:" + ip + ":" + port
            outFile.write(ll + "\n")
            outFile.close()
        except:
            print "---Failure:" + ip + ":" + port
    inFile.close()

def run_check_task():
    check_task()

