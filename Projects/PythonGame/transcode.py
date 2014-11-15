cn=lambda x:x.decode("utf-8")

x=5
y=3

result=x if x<y else y

print result



print [x-y for x,y in zip([0,0,0,3],[0,0,0,4]) if x==y!=0]