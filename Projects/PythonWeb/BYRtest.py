import urllib2
import re

board="WorkLife"
url=r'http://bbs.byr.cn/board/'

url=url+board+'?p='+str(PageNum)

headers = {
        'X-Requested-With': 'XMLHttpRequest', 
        
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36' } 

req=urllib2.Request(url,None,headers)

data=urllib2.urlopen(req).read()

patternString=r'''<a href="/article/'''+board+r'''/(\d+?)"'''

print PatternString

pattern=re.compile(patternString,re.S)
data=data.decode("gbk","ignore").encode("utf-8")
result=re.findall(pattern,data)



