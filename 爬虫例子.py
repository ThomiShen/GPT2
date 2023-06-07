import  requests
import os
from selenium import webdriver
from lxml import etree
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#保存数据图片
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
url=f'https://wenku.baidu.com/view/d4269e8ad4d8d15abe234e2b.html'
r=requests.get(headers=headers,url=url)
r.encoding='GBK'#解决代码乱码问题
data=r.text
# print(data)
parse=etree.HTML(data)
# 定位iframe这个元素
wenben=parse.xpath(('//div[@class="reader-txt-layer"]//p[@class="reader-word-layer reader-word-s1-6"]/text()'))
print(wenben)
