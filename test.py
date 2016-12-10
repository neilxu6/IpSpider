import time
import httplib

inFile = open('proxy.txt','r')
outFile = open('verified.txt', 'w')



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
        time.sleep(2)
        conn.request(method='GET', url=target_url, headers=requestHeader)
        res = conn.getresponse()
        print "+++Success:" + ip + ":" + port
        outFile.write(ll + "\n")
    except:
        print "---Failure:" + ip + ":" + port

inFile.close()
outFile.close()