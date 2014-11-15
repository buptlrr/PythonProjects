# coding=utf-8

# def saveimg(img_data,path,count): 
#      img=img_data[img_data.rfind('.')::] 
#      if(img==".jpg" or img==".png" or img==".gif"): 
#          filepath=path+'/'+str(count)+img 
#          with open(filepath,'wb') as file: 
#              print(img_data) 
#              time.sleep(10) 
#              socket=urllib.urlopen(img_data) 
#              img_data=socket.read() 
#              file.write(img_data) 
#              socket.close() 
#      file.close()


# saveimg('http://www.topit.me/','D:/pythonimage/',10)


import os
import re   #正则模块
import urllib

#获取HTML
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
    
#获取图片URL
def getImg(html):
    reg = r'src="(.*?\.png)"'
    #reg='src=.*.png'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

#下载文件，保存文件
def downloadFile(urllist):
    x = 0
    filepath = "d:\pythonimage3"
    if os.path.exists(filepath) is False:
       os.mkdir(filepath)
    
    for imgurl in urllist:
        temppath = filepath+"\%s.png" % x
        print temppath
        urllib.urlretrieve(imgurl,temppath)
        x+=1
    
if __name__ == "__main__":
    
    html =  getHtml("http://www.pris.net.cn/")
    print html
    #print r"----------------->>获取HTML完毕".decode("utf-8").encode("gbk")      #解决CMD控制台上中文乱码的问题
    urllist =  getImg(html)
    print urllist
    #print r"------------------>>分析URL完毕".decode("utf-8").encode("gbk")
    #downloadFile(urllist)
    #print r"------------------->>文件下载完毕".decode("utf-8").encode("gbk")