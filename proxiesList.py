#coding=utf-8
import random
proxies=[

    'http://178.22.148.122:3129',
    'http://192.99.128.170:8080'
]

proxy={
    'http':proxies[random.randint(0,len(proxies)-1)]
}