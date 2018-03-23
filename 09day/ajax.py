#!/usr/bin/env python
# -*- coding:utf-8 -*-

# $.getJSON(请求逻辑端的URL，回调函数(接受逻辑端返回结果的函数)
"""
 $.getJSON("/list",function(data){
    拿到逻辑端的数据后，对数据处理，一般情况下就是渲染html页

"""
from flask import Flask,request,render_template,redirect,session
import MySQLdb as mysql
import time
import json
import traceback

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('jq_login.html')

@app.route('/userlist')
def list():
    user = {'id':1,'name':'wd','age':18}
    return json.dumps({'code':0,'result':user})

@app.route('/login',methods=['POST'])
def login():
    userinfo = {'name':'fangtao','password':'xiaofang'}
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    print "data=",data
    if data['name'] == userinfo['name'] and data['password'] == userinfo['password']:
        msg = "Hello," + userinfo['name']
        return json.dumps({'code':0,'result':data,'error':msg})
    else:
        msg = "username or password error!"
        return json.dumps({'code':1,'error':msg})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9090,debug=True)
