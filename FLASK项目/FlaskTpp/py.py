from urllib import request,parse
import re
import os
import time

#获取图片数量
def getPicNum(links):
    headers = {
        "Host": " www.mzitu.com",
        "Connection": " keep-alive",
        "Pragma": " no-cache",
        "Cache-Control": " no-cache",
        "Upgrade-Insecure-Requests": " 1",
        "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
        "Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": " zh-CN,zh;q=0.9",
    }
    req=request.Request(url=links,headers=headers)
    response=request.urlopen(req)
    html=response.read().decode("utf-8")
    pattern=re.compile('<span>(\d*)</span>')
    res=pattern.findall(html)
    # print(res)
    # exit()
    pageNum=int(res[4])
    return pageNum




#获取爬取列表
def getList():
    base_url="http://www.mzitu.com/page/{0}/"
    headers={
        "Host": " www.mzitu.com",
        "Connection": " keep-alive",
        "Pragma": " no-cache",
        "Cache-Control": " no-cache",
        "Upgrade-Insecure-Requests": " 1",
        "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
        "Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "http://www.mzitu.com/119965",
        "Accept-Language": " zh-CN,zh;q=0.9",
    }
    allLinks=list()
    for one in range(1,15):
        time.sleep(0.5)
        fullPath=base_url.format(one)
        req=request.Request(url=fullPath,headers=headers)
        response=request.urlopen(req)
        html=response.read().decode("utf-8")
        pattern=re.compile('href="(.*?)"\starget="_blank"><')
        res=pattern.findall(html)
        allLinks=allLinks+res
        # print(res)
        # print("{0}---------------------------------------------".format(one))
    return allLinks

#下载图片
def downloadPic(picPath, fileName,dirName):
    print("downloading...."+fileName)
    headers={
        "Host": " i.meizitu.net",
        "Connection": " keep-alive",
        "Pragma": " no-cache",
        "Cache-Control": " no-cache",
        "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
        "Accept": " image/webp,image/apng,image/*,*/*;q=0.8",
        "Referer": "http://www.mzitu.com/120012",
        "Accept-Language": " zh-CN,zh;q=0.9",

    }
    req=request.Request(url=picPath,headers=headers)
    response=request.urlopen(req)
    context=response.read()
    with open("c:/Users/Michael/Desktop/爬取内容/{dirName}/{fileName}".format(dirName=dirName,fileName=fileName),"wb") as fp:
        fp.write(context)

#获取所图片链接
def getPic(base):
    base_url=base+"/%d"
    headers={
        "Host": " www.mzitu.com",
        "Connection": " keep-alive",
        "Pragma": " no-cache",
        "Cache-Control": " no-cache",
        "Upgrade-Insecure-Requests": " 1",
        "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
        "Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": " zh-CN,zh;q=0.9",
        # "Cookie": " Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1518425004; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1518425648",
    }
    dirName=base_url.split("/")[-2]
    if not os.path.exists("c:/Users/Michael/Desktop/爬取内容/{dirName}/".format(dirName=dirName)):
        os.makedirs("c:/Users/Michael/Desktop/爬取内容/{dirName}/".format(dirName=dirName))
    count=getPicNum(base)
    for one in range(1,count):
        time.sleep(0.5)
        fullUrl=base_url% one
        req=request.Request(url=fullUrl,headers=headers)
        response=request.urlopen(req)
        html=response.read().decode("utf-8")
        pattern=re.compile('img.*?src="(.*?)"')
        res=pattern.search(html)
        # print(res.group(1))
        if res is not None:
            picPath=res.group(1)
            fileName=picPath.split("/")[-1]
            # print("c:/Users/Michael/Desktop/{dirName}/fileName".format(dirName=dirName))
            # exit()
            downloadPic(picPath,fileName,dirName)
            # request.urlretrieve(picPath,"c:/Users/Michael/Desktop/{dirName}/{fileName}".format(dirName=dirName,fileName=fileName),headers)
        else:
            print("第{0}页没有图片".format(one))
        # print(res)0

        print(one,"------------------------------------------------------------------------")
    print("下载完毕")



if __name__ == '__main__':
    allLinks=getList()
    for one in allLinks:
        getPic(one)