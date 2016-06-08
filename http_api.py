#!/usr/bin/env python
#coding:utf-8
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
app = Flask(__name__)
status = [
    {
        'status': 200,
        'info': '发送成功'
    }
]
errstatus = [
    {   
        'status': 201,
        'info': '不支持GET方式'
    }
]

@app.route('/', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        tos = request.form.get('phone')
        content = request.form.get('content')
        return jsonify({'resp':status})
    elif request.method == 'GET':
        return jsonify({'resp':errstatus})
    else:
        return jdonigy({'resp':'unknown method'})
@app.route('/qcor')
def qcor():
    return  '<html><img src=./static/default.jpg></html>'

def runserver():
    app.run(port=5001,host='0.0.0.0',debug=True)

