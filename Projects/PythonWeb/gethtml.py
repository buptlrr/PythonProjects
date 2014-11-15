

# coding=utf-8
import urllib2
import urllib

url=r"http://l007rr:lrr123456@nforum.byr.edu.cn/byr/api/widget/topten.json"

# print url
# req=urllib2.Request(url)
respone=urllib2.urlopen(url)
a=respone.read()
print a
#urllib.urlretrieve(url,"D:\\aaa.txt")