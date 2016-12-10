#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import httplib
import threading



def verifyProxyList():
    requestHeader ={
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"
    }

    target_url = 'http://www.baidu.com/'

    while True:
        lock.acquire()
        ll = inFile.readline().strip()
        lock.release()
        if len(ll) == 0: break
        line = ll.strip().split(':')
        ip=line[0]
        port = line[1]
        try:
            conn = httplib.HTTPConnection(ip, port, timeout=5.0)
            time.sleep(1)
            conn.request(method='GET', url=target_url, headers=requestHeader)
            res = conn.getresponse()
            lock.acquire()
            print "+++Success:" + ip + ":" + port
            outFile.write(ll + "\n")
            lock.release()
        except:
            print "---Failure:" + ip + ":" + port


if __name__ == '__main__':
    inFile = open('proxy.txt','r')
    outFile = open('verified.txt', 'w')
    lock = threading.Lock()

    all_thread = []
    for i in range(30):
        t = threading.Thread(target=verifyProxyList)
        all_thread.append(t)
        t.start()

    for t in all_thread:
        t.join()

    inFile.close()
    outFile.close()
    print "All Done."