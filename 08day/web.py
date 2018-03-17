#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作业：
# 1. 验证用户是否登录，如果没有登录，跳转到登录页面
# 2. 验证角色，不同角色操作不同的方法

from flask import Flask,request,render_template,redirect,session
import MySQLdb as mysql
import time
import json
import traceback

app = Flask(__name__)
app.secret_key="1q2w3e4R"

db = mysql.connect(user='root',passwd='xiaofang',db='reboot')
cur = db.cursor()

@app.route('/')
def index():
    if not session.get('name',None):
        return redirect('/login')
    return redirect('/userlist')
    
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        if not data.get('name',None) or not data.get('password',None):
            errmsg = "name or password not null"
            return render_template('login.html',error=errmsg)
        fields = ['name','password','role']
        sql = "select %s from users where name='%s'" % (','.join(fields),data['name'])
        cur.execute(sql)
        res = cur.fetchone()
        if not res:       #如果这个用户在数据库中不存在，返回的结果就是res=(())
            errmsg = "%s is not exist" % data['name']
            return render_template('login.html',error=errmsg)
        user = {}
        user = dict((k,res[i]) for i,k in enumerate(fields))
        if user['password'] != data['password']:
            errmsg = "password is wrong"
            return render_template('login.html',error=errmsg)
        else:
            session['name'] = user['name']
            session['role'] = user['role']
            return redirect('/userlist')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('name')
    session.pop('role')
    return redirect('/login')

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

@app.route('/delete',methods=['GET'])
def delete():
    if not session.get('name',None):
        return redirect('/login')
    id = request.args.get('id',None)
    if not id:
        errmsg = "must have id"
        return render_template("userlist.html",error=errmsg)
    try:
        sql = "delete from users where id = %s" % id
        cur.execute(sql)
        return redirect('/userlist')
    except Exception,e:
        errmsg = e
        return render_template("userlist.html",error=errmsg)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)
