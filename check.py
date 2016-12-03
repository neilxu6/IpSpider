#!/usr/bin/env python
# -*- coding: utf-8 -*-



import httplib
import threading

inFile = open('proxy.txt')
outFile = open('verified.txt', 'w')
lock = threading.Lock()

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
        line = ll.strip().split('|')
        protocol = line[5]
        ip = line[1]
        port = line[2]

        try:
            conn = httplib.HTTPConnection(ip, port, timeout=5.0)
            conn.request(method='GET', url=target_url, headers=requestHeader)
            res = conn.getresponse()
            lock.acquire()
            print "+++Success:" + ip + ":" + port
            outFile.write(ll + "\n")
            lock.release()
        except:
            print "---Failure:" + ip + ":" + port


if __name__ == '__main__':
    tmp = open('proxy.txt', 'w')
    tmp.write("")
    tmp.close()
    proxynum = getProxyList("http://www.xicidaili.com/nn/")
    print u"国内高匿：" + str(proxynum)
    proxynum = getProxyList("http://www.xicidaili.com/nt/")
    print u"国内透明：" + str(proxynum)
    proxynum = getProxyList("http://www.xicidaili.com/wn/")
    print u"国外高匿：" + str(proxynum)
    proxynum = getProxyList("http://www.xicidaili.com/wt/")
    print u"国外透明：" + str(proxynum)

    print u"\n验证代理的有效性："

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