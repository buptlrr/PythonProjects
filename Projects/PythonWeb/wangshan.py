import re
import urllib2
import urllib



for i in range(100,208):
	url="http://www.hbhz.net/UserList.asp?OrderType=1&page="
	url+=str(i)
	req=urllib2.Request(url)
	response=urllib2.urlopen(req)
	urlresult=response.read()
	#print urlresult
	result=re.search(r'1455624058',urlresult)
	if result:
		print i
		break
else:
	print "not found"




