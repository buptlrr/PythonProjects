#coding=utf-8
import re
with open("a.txt",'r') as f:
	result=f.read()

result=result.decode('gbk','ignore').encode('utf-8')


#result=repl(result).decode('utf-8')
print result
tnump='通信'
tnump=tnump.decode('utf-8')
tnump=tnump.encode('gbk')
print tnump
pattern1=re.compile(tnump)
pattern=re.compile(r'<tr class="odd".*?<td.*?(\d+).*?<td.*?(\d+|null).*?<td.*?<td.*?">.*?(\w[\w ]+).*?<td.*?([\d\.]+).*?<td.*?<td.*?(\d+\.\d+|免修)',re.S)
c=re.findall(r'中等',result)

print c