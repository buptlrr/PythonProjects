#coding="utf-8"

import urllib2
import re

url="http://www.weather.com.cn/data/cityinfo/101010100.html"

req=urllib2.Request(url)

data=urllib2.urlopen(req).read()

pattern=re.compile(r'city":"(.*?)".*?temp1":"(.*?)"',re.S)

result=re.findall(pattern,data)

for i in result:
	for k in i:
		print k.decode("utf-8")