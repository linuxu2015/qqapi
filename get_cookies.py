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
    DstDir = "E:\\qqapi\\img\\"
    #DstDir = "/opt/qqapi/img/"
    print "save"
    with open(DstDir+imgName ,"wb") as jpg:
        jpg.write(image)
       # return
    jpg.close
    return cookies
cookies = saveImage()
print cookies
time.sleep(10)
session = requests.Session()
verify_erwei = 'https://ssl.ptlogin2.qq.com/ptqrlogin?webqq_type=10&remember_uin=1&login2qq=1&aid=501004106%20&u1=http%3A%2F%2Fw.qq.com%2Fproxy.html%3Flogin2qq%3D1%26webqq_type%3D10%20&ptredirect=0&ptlang=2052&daid=164&from_ui=1&pttype=1&dumy=&fp=loginerroralert%20&action=0-0-157510&mibao_css=m_webqq&t=1&g=1&js_type=0&js_ver=10143&login_sig=&pt_randsalt=0'
res = session.get(verify_erwei,cookies=cookies)
data = str(res.text)
print data
str_url = data.split(',')[2]
url = str_url.strip("'")
print url
'''
ptuiCB('0','0',
'http://ptlogin4.web2.qq.com/check_sig?pttype=1&uin=371044414&service=ptqrlogin&nodirect=0&ptsigx=565553cbc69d8e4fc89170aa0b323c2297d5a5ffc4cd428956ef9be0f2b23f6069b410aeda438d123318f236fa5c561263367e3f98b1c1a2698f3c0075b1bfce&s_url=http%3A%2F%2Fw.qq.com%2Fproxy.html%3Flogin2qq%3D1%26webqq_type%3D10%20&f_url=&ptlang=2052&ptredirect=100&aid=501004106&daid=164&j_later=0&low_login_hour=0&regmaster=0&pt_login_type=3&pt_aid=0&pt_aaid=16&pt_light=0&pt_3rd_aid=0
','0','登录成功！', '那颗星');

'''

##获取ptwebqq
res = session.get(url)
#print res.text
new_cookies = session.cookies
cookies_file = open("E:\\qqapi\\img\\cookies_file.pkl","wb")
pk.dump(new_cookies,cookies_file,True)
