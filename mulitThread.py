# -*- coding: utf-8 -*-

import time
import threading

# 重写run方法
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print 'threadName={},threadNumber={}'.format(self.name,i)
            time.sleep(1)

# 创建线程
def main():
    print '开始启动线程...'
    thread=[MyThread()for i in range(3)]
    for t in thread:
        t.start()
    print '启动线程完毕!'
    print '开始加入线程...'
    for t in thread:
        t.join()
    print '加入线程完毕！'

# 加入线程锁
lock=threading.Lock()
# 获取锁



