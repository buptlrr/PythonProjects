from urllib2 import Request, urlopen, URLError, HTTPError


old_url = 'http://www.weibo.com'
req = Request(old_url)
response = urlopen(req)
print 'Old url :' + old_url
print 'Real url :' + response.geturl()
