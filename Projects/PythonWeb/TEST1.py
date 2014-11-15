#coding=utf-8
#---------------------------------------   
# 作者：李热热
# 名称：北京邮电大学学生成绩绩点计算器
#---------------------------------------  

#abcoBXO2cv_o46Ug2fqLu abcoBXO2cv_o46Ug2fqLu abcP5cxm41h7sfmMQzsLu

import urllib2
import urllib
import cookielib  
import re
cookie = cookielib.CookieJar()    
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  

login_user='09210326'
login_pw='09210326'

login_url = 'http://jwxt.bupt.edu.cn/jwLoginAction.do'  



request_type='Content-Type: application/x-www-form-urlencoded\n\r'
request_length='Content-Length: 31\n\r'
request_content="type=sso&zjh="+login_user+"&mm="+login_pw+"\n\r"

post_request=request_type+request_length+'\n\r'+request_content
 
postdata=urllib.urlencode({    
    'type':'sso',    
    'zjh':login_user,
    'mm' :login_pw    
})  



# headers = {
		  
# 		  'Cookie': 'JSESSIONID=abcxcJua-BDg37VKK_pLu'
#           }  

#data = urllib.urlencode(values) # 编码工作
req = urllib2.Request(login_url,postdata)#,headers)  # 发送请求同时传data表单

response =opener.open(req)
the_page = response.read()  #读取反馈的内容

#result=opener.open("http://jwxt.bupt.edu.cn/gradeLnAllAction.do")
print the_page
#print result
for item in cookie:
	print item.name
	print item.value

#url = "http://jwxt.bupt.edu.cn/gradeLnAllAction.do?type=ln&oper=fainfo&fajhh=223"
url="http://jwxt.bupt.edu.cn/gradeLnAllAction.do?type=ln&oper=fainfo"

req = urllib2.Request(url)
print req

reponse=opener.open(req)
result=reponse.read()
print result

with open("a.txt",'w') as f:
	f.write(result)

result=result.decode("gbk",'ignore').encode("utf-8")
print result

#<addinfourl at 37015304 whose fp = <socket._fileobject object at 0x0234AC70>>

pattern=re.compile(r'<tr class="odd".*?<td.*?(\d+).*?<td.*?(\d+|null).*?<td.*?<td.*?">.*?(\w[\w ]+(?:\xe2\x85\xa0|\xe2\x85\xa1|\xe2\x85\xa3)?).*?<td.*?([\d\.]+).*?<td.*?<td.*?(\xe5\x85\x8d\xe4\xbf\xae|\xe4\xb8\xad\xe7\xad\x89|\d+\.\d+)',re.S)
re_result=re.findall(pattern,result)

print re_result,len(re_result)

GPA=0
mark=0
Gmark=0
for index,item in enumerate(re_result):
	Gmark+=(float)(item[3])
	if item[4]=="免修" or item[4]=="中等":
		print (float)(item[3]),item[2],item[4],index
	else:
		GPA+=(float)(item[3])*(float)(item[4])
		mark+=(float)(item[3])
		print (float)(item[3]),item[2],item[4],index
else:
	GPA/=mark

print GPA,Gmark