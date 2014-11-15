import urllib
import urllib2

url="http://www.baidu.com/s?"

data={"word":"Jecvay Notes"}

getdata=urllib.urlencode(data)
full_url=url+getdata


req=urllib2.Request(full_url)
result=urllib2.urlopen(req).read()#.decode("utf-8")

print result