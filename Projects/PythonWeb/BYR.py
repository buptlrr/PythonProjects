#coding=utf-8
import json
import urllib2
from math import floor
import re

FoundArticle = {}
FoundArticle1 = []
FoundArticle2 = []

board = 'WorkLife'
PageNum = 0
PatternString = r'''<a href="/article/'''+board+r'''/(\d+?)"'''



ArticlePatternString = '发信人: '
ArticleSender = 'baobaoshan'
ArticlePatternString += ArticleSender

ArticlePatternString1 = '阿里'
ArticlePatternString2 = '面试'

ArticlePatternString3 = '前端'

option = 1


for PageNum in xrange(1,2):
	url = r'http://bbs.byr.cn/board/'
	
	url = url+board+'?p='+str(PageNum)

	print url

	headers = {
	        'X-Requested-With': 'XMLHttpRequest', 
	        
	        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36' } 

	req = urllib2.Request(url,None,headers)
	try:
		data = urllib2.urlopen(req).read()
	except:
		continue
	#print data.decode("gbk","ignore")
	
	pattern = re.compile(PatternString,re.S)
	data = data.decode("gbk","ignore").encode("utf-8")
	result = re.findall(pattern,data)
	
	print result
	if option == 0:
		for num in result:
			ArticleUrl = "http://bbs.byr.cn/article/"+board+"/"+str(num)
			print "---------------------正在抓取---------------------",ArticleUrl
			req = urllib2.Request(ArticleUrl,None,headers)
			try:
				PageNumData = urllib2.urlopen(req).read()
			except:
				continue
			#print PageNumData.decode("gbk")
			PageNumPattern = re.compile(r'<i>(\d+?)</i>')
			TieNum = re.search(PageNumPattern,PageNumData)
			
			ArticlePageNum = int(floor(int(TieNum.group(1))/10.0)+1)

			for i in xrange(1,ArticlePageNum+1):
				ArticleUrl = "http://bbs.byr.cn/article/"+board+"/"+str(num)
				ArticleUrl = ArticleUrl+'?p='+str(i)
				print ArticleUrl

				req = urllib2.Request(ArticleUrl,None,headers)
				try:
					data = urllib2.urlopen(req).read()
				except:
					continue


				pattern = re.compile(ArticlePatternString,re.S)
				data = data.decode("gbk","ignore").encode("utf-8")
				match = re.search(ArticlePatternString,data)
			
				if match:
					if 	FoundArticle.get(num) == None:
						FoundArticle[num] = []
					FoundArticle[num].append(i)
	elif option == 1:
		for num in result:
			ArticleUrl = "http://bbs.byr.cn/article/"+board+"/"+str(num)
			print "---------------------正在抓取---------------------",ArticleUrl
			req = urllib2.Request(ArticleUrl,None,headers)
			try:
				data = urllib2.urlopen(req).read()
			except:
				continue
			
			pattern = re.compile(ArticlePatternString1,re.S)
			data = data.decode("gbk","ignore").encode("utf-8")
			match1 = re.search(ArticlePatternString1,data)
	
			pattern = re.compile(ArticlePatternString2,re.S)

			
			match2 = re.search(ArticlePatternString2,data)
			pattern = re.compile(ArticlePatternString3,re.S)
			
			match3 = re.search(ArticlePatternString3,data)

			if match1 and match2 and match3:
				FoundArticle1.append(num)

#print FoundArticle1
board = 'Job'
PatternString = r'''<a href="/article/'''+board+r'''/(\d+?)"'''

for PageNum in xrange(311,341):
	url = r'http://bbs.byr.cn/board/'
	
	url = url+board+'?p='+str(PageNum)

	print url

	headers = {
	        'X-Requested-With': 'XMLHttpRequest', 
	        
	        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36' } 

	req = urllib2.Request(url,None,headers)
	try:
		data = urllib2.urlopen(req).read()
	except:
		continue
	
	pattern = re.compile(PatternString,re.S)
	data = data.decode("gbk","ignore").encode("utf-8")
	result = re.findall(pattern,data)
	print result
	if option == 0:
		for num in result:
			ArticleUrl = "http://bbs.byr.cn/article/"+board+"/"+str(num)
			print "---------------------正在抓取---------------------",ArticleUrl
			req = urllib2.Request(ArticleUrl,None,headers)
			try:
				PageNumData = urllib2.urlopen(req).read()
			except:
				continue
			#print PageNumData.decode("gbk")
			PageNumPattern = re.compile(r'<i>(\d+?)</i>')
			TieNum = re.search(PageNumPattern,PageNumData)
			
			ArticlePageNum = int(floor(int(TieNum.group(1))/10.0)+1)

			for i in xrange(1,ArticlePageNum+1):
				ArticleUrl = "http://bbs.byr.cn/article/"+board+"/"+str(num)
				ArticleUrl = ArticleUrl+'?p='+str(i)
				print ArticleUrl

				req = urllib2.Request(ArticleUrl,None,headers)
				try:
					data = urllib2.urlopen(req).read()
				except:
					continue

				pattern = re.compile(ArticlePatternString,re.S)
				data = data.decode("gbk","ignore").encode("utf-8")
				match = re.search(ArticlePatternString,data)
			
				if match:
					if 	FoundArticle.get(num) == None:
						FoundArticle[num] = []
					FoundArticle[num].append(i)
	elif option == 1:

		for num in result:
			ArticleUrl = "http://bbs.byr.cn/article/"+board+"/"+str(num)
			print "---------------------正在抓取---------------------",ArticleUrl
			req = urllib2.Request(ArticleUrl,None,headers)
			try:
				data = urllib2.urlopen(req).read()
			except:
				continue
			pattern = re.compile(ArticlePatternString1,re.S)
			data = data.decode("gbk","ignore").encode("utf-8")
			match1 = re.search(ArticlePatternString1,data)
			pattern = re.compile(ArticlePatternString2,re.S)
			
			match2 = re.search(ArticlePatternString2,data)
			pattern = re.compile(ArticlePatternString3,re.S)
			
			match3 = re.search(ArticlePatternString3,data)

			if match1 and match2 and match3:
				FoundArticle2.append(num)




			#print PageNumData.decode("gbk")
			



#print FoundArticle
print FoundArticle1
print FoundArticle2