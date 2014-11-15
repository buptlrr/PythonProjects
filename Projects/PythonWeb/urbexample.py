# coding=utf-8
import urllib2
import urllib
import base64
 #urllib.urlretrieve('http://www.itzcn.com','D:\\aa.txt')

# req=urllib2.Request('http://www.bupt.edu.cn')

# response = urllib2.urlopen(req)
# html = response.read()
# print html

login_user='admin'
login_pw='admin'

auth='Basic '+base64.b64encode(login_user+':'+login_pw)

print auth
url = 'http://192.168.1.1/cgi-bin-igd/reboot.cgi'  

url_1='http://192.168.1.1/cgi?7'

request='[ACT_REBOOT#0,0,0,0,0,0#0,0,0,0,0,0]0,0\r\n'
  
headers = {
		  'Authorization' : auth,
		  'Referer'       : 'http://192.168.1.1/'
          }  

#data = urllib.urlencode(values) # 编码工作
req = urllib2.Request(url_1,request,headers)  # 发送请求同时传data表单
response = urllib2.urlopen(req)  #接受反馈的信息
the_page = response.read()  #读取反馈的内容
print the_page
		

