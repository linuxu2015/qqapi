#!/usr/bin/env python
#coding:utf-8
import time
import requests
import json
import sys
import headers
import random
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
for item in  new_cookies:
	if item.name == 'ptwebqq':
		ptwebqq = item.value
print ptwebqq

session.headers = headers.get_ptwebqq

ti = int(time.time()*1000)
url = 'http://s.web2.qq.com/api/getvfwebqq?ptwebqq=%s&clientid=53999199&psessionid=&t=%s' %(ptwebqq,ti)
res = session.get(url,cookies=new_cookies)

data = json.loads(res.text)
#print data
vfwebqq = data['result']['vfwebqq']
print vfwebqq
session = requests.Session()
session.headers = headers.get_psessionid
data ={
 "ptwebqq": ptwebqq,
  "clientid": 53999199,
  "psessionid": "",
  "status": "online",
}
r = json.dumps(data)
a = session.post('http://d1.web2.qq.com/channel/login2',cookies=new_cookies,data={"r":r})
data = json.loads(a.text)
print data
psessionid = data['result']['psessionid']
print psessionid
session = requests.Session()
session.headers = headers.send_msg
status = True
while status:
    msg_id = int(random.random()*100000000)
    msg = {
    "to":371044414,
    "content":"[\"test……\",[\"font\",{\"name\":\"宋体\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]",
    "face":549,
    "clientid":53999199,
    "msg_id":msg_id,
    "psessionid":psessionid
    }
    a = session.post('http://d1.web2.qq.com/channel/send_buddy_msg2',cookies=new_cookies,data = {"r":json.dumps(msg)})
    print a.text
    if "ok" in a.text:
        status = False
        print "send sussess"
        break
    else:
        status = True
        print "send failed"
        time.sleep(5)
