# coding=utf-8
import urllib
import re
import os
def func():
    #正则表达式
    #本实例中的嵌套网址是非标准的，所以在后面进行了处理，
    p=re.compile('(?<=<a href=")\d{8,}.html')
    img=re.compile('(?<=<img src=")http://img.21zw.net/64/64753/\d{4,}/\d{4,}.gif')
    #初始网页，包含多个子网页
    html_src = urllib.urlopen('http://www.21zw.net/book/64/64753/index.html').read()
    m=p.findall(html_src)

    #对所抓取的网页遍历
    for addr in m:
        s='http://www.21zw.net/book/64/64753/'+addr
        subUrl_src=urllib.urlopen(s).read()
        photo=img.findall(subUrl_src)
        #遍历图片
        for pp in photo:
            folder="C://pic"
            # pic_name=pp.split('/')[-1]
            # if os.path.exists(folder)==False:
            #     os.makedirs(folder)
            #保存图片
            try:
                url_file=urllib.urlopen(pp)
                f=open(folder+'/'+pic_name,'wb')
                while True:
                    r=url_file.read(1024)
                    if not r:
                        break
                    f.write(r)
                f.close()
            except:
                print "噢，保存图片出现问题。。。"
                print "Unexpected error:"+sys.exc_info()[0]+sys.exc_info()[1]
            else:
                print "保存图片成功。。。"
if __name__=="__main__":
    func()
  
