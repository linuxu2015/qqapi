#!/usr/bin/env python
#coding:utf-8
import time
import requests
import json
import sys
import headers
import random
import cPickle as pk
reload(sys)
sys.setdefaultencoding('utf-8')
def saveImage(imgName = 'default.jpg'):
    session = requests.Session()
    imgurl = 'https://ssl.ptlogin2.qq.com/ptqrshow?appid=501004106&e=0&l=M&s=5&d=72&v=4&t=0.3835296393318739'
    response = session.get(imgurl,stream=True)
    cookies = session.cookies
    print cookies
    print response
    image = response.content
    #DstDir = "E:\\qqapi\\img\\"
    DstDir = "/opt/qqapi/img/"
    print "save"
    with open(DstDir+imgName ,"wb") as jpg:
        jpg.write(image)
       # return
    jpg.close
    return cookies
cookies = saveImage()
session = requests.Session()
verify_erwei = 'https://ssl.ptlogin2.qq.com/ptqrlogin?webqq_type=10&remember_uin=1&login2qq=1&aid=501004106%20&u1=http%3A%2F%2Fw.qq.com%2Fproxy.html%3Flogin2qq%3D1%26webqq_type%3D10%20&ptredirect=0&ptlang=2052&daid=164&from_ui=1&pttype=1&dumy=&fp=loginerroralert%20&action=0-0-157510&mibao_css=m_webqq&t=1&g=1&js_type=0&js_ver=10143&login_sig=&pt_randsalt=0'
status = True
while status:
    res = session.get(verify_erwei,cookies=cookies)
    data = str(res.text)
    if 'http' not in data:
        print "等待扫描二维码"
        print "访问http://192.168.100.145:8080/default.jpg扫描二维码"
        time.sleep(2)
    else:
        str_url = data.split(',')[2]
        url = str_url.strip("'")
        res = session.get(url)
        new_cookies = session.cookies
        #cookies_file = open("E:\\qqapi\\img\\cookies_file.pkl","wb")
        cookies_file = open("/opt/qqapi/img/cookies_file.pkl","wb")
        pk.dump(new_cookies,cookies_file,True)
	status = False
        print "二维码扫描成功"
