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
    imgurl = 'https://ssl.ptlogin2.qq.com/ptqrshow?appid=501004106&e=0&l=M&s=5&d=72&v=4&t=0.3835296393318739'
    response = requests.get(imgurl,stream=True)
    print response
    image = response.content
    #DstDir = "F:\\image\\"
    DstDir = "/opt/qqapi/img/"
    print "save"
    with open(DstDir+imgName ,"wb") as jpg:
        jpg.write(image)
        return
    jpg.close
#saveImage()

session = requests.Session()
session.headers = headers.get_ptwebqq
ti = int(time.time()*1000)
url = 'http://s.web2.qq.com/api/getvfwebqq?ptwebqq=d68fcef50716c3fa75c216de0b9a0b08ee83c989d19dee336b0421e74a671caf&clientid=53999199&psessionid=&t=%s' %ti
res = session.get(url)
data = json.loads(res.text)
vfwebqq = data['result']['vfwebqq']
#print vfwebqq
session = requests.Session()
session.headers = headers.get_psessionid
data ={
 "ptwebqq": "d68fcef50716c3fa75c216de0b9a0b08ee83c989d19dee336b0421e74a671caf",
  "clientid": 53999199,
  "psessionid": "",
  "status": "online",
}
r = json.dumps(data)
a = session.post('http://d1.web2.qq.com/channel/login2',data={"r":r})
data = json.loads(a.text)
psessionid = data['result']['psessionid']
#print psessionid
session = requests.Session()
session.headers = headers.send_msg
msg_id = int(random.random()*100000000)
msg = {
"to":3541204146,
"content":"[\"邵永……\",[\"font\",{\"name\":\"宋体\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]",
"face":549,
"clientid":53999199,
"msg_id":msg_id,
"psessionid":psessionid
}
status = True
while status:
    a = session.post('http://d1.web2.qq.com/channel/send_buddy_msg2',data = {"r":json.dumps(msg)})
    if "ok" in a.text:
        status = False
        print "send sussess"
        break
    else:
        status = True
        print "send failed"
        time.sleep(5)
     
