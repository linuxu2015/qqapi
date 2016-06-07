#!/usr/bin/env python
#coding:utf-8
import  requests
import random
import headers
import json
import cPickle as pk
import time
cookies_file = file("E:\\qqapi\\img\\cookies_file.pkl","rb")
new_cookies = pk.load(cookies_file)
for item in  new_cookies:
	if item.name == 'ptwebqq':
		ptwebqq = item.value
# print ptwebqq
session = requests.Session()
session.headers = headers.get_ptwebqq

ti = int(time.time()*1000)
url = 'http://s.web2.qq.com/api/getvfwebqq?ptwebqq=%s&clientid=53999199&psessionid=&t=%s' %(ptwebqq,ti)
res = session.get(url,cookies=new_cookies)

data = json.loads(res.text)
#print data
vfwebqq = data['result']['vfwebqq']
# print vfwebqq
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
# print data
psessionid = data['result']['psessionid']
# print psessionid
session = requests.Session()
session.headers = headers.send_msg
date = time.asctime()
status = True
while status:
    msg_id = int(random.random()*100000000)
    msg = {
        "group_uin":3920456119,
        "content":"[\"测试\",[\"font\",{\"name\":\"宋体\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]",
        "face":543,
        "clientid":53999199,
        "msg_id":msg_id,
        "psessionid":psessionid
    }
    a = session.post('http://d1.web2.qq.com/channel/send_qun_msg2',cookies=new_cookies,data = {"r":json.dumps(msg)})
    print a.text
    if "ok" in a.text:
        status = False
        print "send sussess"
        break
    else:
        status = True
        print "send failed"
        # time.sleep(5)