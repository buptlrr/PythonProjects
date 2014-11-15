#coding=utf-8
import re
import urllib2
import urllib
import cookielib
from collections import deque

queue = deque()
visited = set()
url = 'http://news.dbanotes.net'
queue.append(url)
cnt = 0

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  


while queue:
  url = queue.popleft()  # 队首元素出队
  visited |= {url}  # 标记为已访问
 
  print '已经抓取:',str(cnt),'   正在抓取 <---  ',url
  cnt += 1
  
  #print urlop.info()
  headers={'Connection': 'Keep-Alive','Accept': 'text/html, application/xhtml+xml, */*','Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3','User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
  try:
    req=urllib2.Request(url,None,headers)
    urlop = opener.open(req,timeout=1000)
  except:
    continue
  if 'html' not in urlop.info().getheader('Content-Type'):
    continue
  
  #避免程序异常中止, 用try..catch处理异常
  try:
    data = urlop.read()#decode('utf-8')
  except:
    continue
 
  # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
  linkre = re.compile(r'href="(.+?)"')
  for x in linkre.findall(data):
    if 'http' in x and x not in visited:
      queue.append(x)

      print '加入队列 --->',x
