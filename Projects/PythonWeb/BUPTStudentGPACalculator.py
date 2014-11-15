#coding=utf-8
#------------------------------------------  
# 作者：李热热
# 名称：北京邮电大学学生成绩绩点计算器v1.0
# 注：在成绩中只考虑了分数、中等、免修
#------------------------------------------ 
import urllib2
import urllib
import cookielib  
import re

class SDU_GPA:
	login_url = 'http://jwxt.bupt.edu.cn/jwLoginAction.do'
	result_url = "http://jwxt.bupt.edu.cn/gradeLnAllAction.do?type=ln&oper=fainfo"
	cookie = cookielib.CookieJar()
	pattern=re.compile(r'<tr class="odd".*?<td.*?(\d+).*?<td.*?(\d+|null).*?<td.*?<td.*?">.*?(\w[\w ]+(?:\xe2\x85\xa0|\xe2\x85\xa1|\xe2\x85\xa3)?).*?<td.*?([\d\.]+).*?<td.*?<td.*?(\xe5\x85\x8d\xe4\xbf\xae|\xe4\xb8\xad\xe7\xad\x89|\d+\.\d+)',re.S)
	GPA=0
	mark=0
	Gmark=0

	#申明成员变量
	def __init__(self,ID,Pw):
		self.login_user = ID
		self.login_pw = Pw
		self.postdata = urllib.urlencode({'type':'sso','zjh':self.login_user,'mm':self.login_pw})  
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
	def sdu_init(self,save=0,view=1):
		self.req = urllib2.Request(self.login_url,self.postdata)
		self.response = self.opener.open(self.req)
		self.the_page = self.response.read()
		self.sdu_getmark(save)
		self.sdu_re(self.result)
		self.sdu_GPA(self.re_result,view)
	
	def sdu_getmark(self,save):
		self.req = urllib2.Request(self.result_url)
		self.reponse=self.opener.open(self.req)
		self.result=self.reponse.read()
		if save:
			with open("a.txt",'w') as f:
				f.write(self.result)
		else:
			pass
		self.result=self.result.decode("gbk",'ignore').encode("utf-8")
	
	def sdu_re(self,result):
		self.re_result=re.findall(self.pattern,result)		
	
	def sdu_GPA(self,re_result,view):
		for index,item in enumerate(re_result):
			self.Gmark+=(float)(item[3])
			if item[4]=="免修" or item[4]=="中等":
				if view:
					print (float)(item[3]),item[2],item[4],index
				else:
					pass
			else:
				self.GPA+=(float)(item[3])*(float)(item[4])
				self.mark+=(float)(item[3])
				if view:
					print (float)(item[3]),item[2],item[4],index
				else:
					pass
		else:
			self.GPA/=self.mark

	def sdu_print(self):
		print "GPA:",self.GPA,"总学分",self.Gmark,"通过门数",len(self.re_result)

if __name__=="__main__":
	s=SDU_GPA("09210326","09210326")
	s.sdu_init()
	s.sdu_print()