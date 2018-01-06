#!/usr/bin/env python
# -*- coding:utf-8 -*-

# jQuery的基本三步走：
# 1. 选择器--找到需要操作的元素
# 2. 操作--DOM元素进行增删改查
#   2.1：操作html文档内容--常用元素 table form div等
#   2.2：操作html元素属性--常用属性
#   2.3：操作html元素的样式--css（其实也属于属性）
# 3. 事件--什么情况下触发jQuery的操作，ajax等


# 1. 定义 <div id="loginForm">
# 2. 调用 $('#loginForm')
# $(selector).action()
# $:表示jQuery
# selector：选择器（选定HTML元素）
# action(): 选定之后，对这个元素的操作
#     val()：操作表单的值
#     html(): 操作元素
#     attr(): 操作属性

from flask import Flask,request,render_template,redirect,session
import MySQLdb as mysql
import time
import json
import traceback

app = Flask(__name__)
app.secret_key="1q2w3e4R"

db = mysql.connect(user='root',passwd='xiaofang',db='reboot')
cur = db.cursor()

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        if not data.get('name',None) or not data.get('password',None):
            errmsg = "name or password not null"
            #return render_template('login.html',error=errmsg)
            return json.dumps({'code':'1','error':errmsg})
        fields = ['name','password','role']
        sql = "select %s from users where name='%s'" % (','.join(fields),data['name'])
        cur.execute(sql)
        res = cur.fetchone()
        if not res:       #如果这个用户在数据库中不存在，返回的结果就是res=(())
            errmsg = "%s is not exist" % data['name']
            #return render_template('login.html',error=errmsg)
        user = {}
        user = dict((k,res[i]) for i,k in enumerate(fields))
        if user['password'] != data['password']:
            errmsg = "password is wrong"
            #return render_template('login.html',error=errmsg)
        else:
            session['name'] = user['name']
            session['role'] = user['role']
            #return redirect('/userlist')
            return json.dumps({'code':'0','error':"login success"})
    else:
        return render_template('login.html')

@app.route('/userlist')
def userlist():
    if not session.get('name',None):
        return redirect('/login')
    users = []
    fields = ['id','name','name_cn','email','mobile']
    try:
	sql = "select %s from users" % ','.join(fields)
	cur.execute(sql)
	res = cur.fetchall()
	users = [dict((k,row[i]) for i,k in enumerate(fields)) for row in res]
        return render_template('userlist.html',users=users)
    except Exception,e:
	errmsg = e
	return render_template('userlist.html',error=errmsg)

@app.route('/delete')
def delete():
    if not session.get('name',None):
        return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('name')
    return redirect('/login')






if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)
