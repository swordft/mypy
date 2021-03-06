#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作业 用户管理（基于文件存储）

# 1. 管理员登录（写死账号是admin 密码是pwd）
# 2. 登录之后，看到用户和密码列表（存储在文件中），支持添加、删除、修改密码的操作

from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
from datetime import datetime
app = Flask(__name__)

db = mysql.connect(user='root',passwd='xiaofang',db='reboot')
cur = db.cursor()

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login',methods=['POST','GET'])
def auth():
    if request.method == "POST":
        user = request.form.get('username')
        pwd = request.form.get('password')
        if user == "fangtao" and pwd == "xiaofang":
            return redirect('/userlist')
        else:
            return render_template('login.html',error="username or password error!")    
    else:
        return render_template('login.html')

@app.route('/userlist')
def user():
    fields = ['id','name','password','email','mobile']
    sql = "select %s from users" % ','.join(fields)
    cur.execute(sql)
    res = cur.fetchall()
    users = []
    for row in res:
        user = {}
        for i,k in enumerate(fields):
	    user[k] = row[i]
	users.append(user)
    return render_template('userlist.html',users=users)

@app.route('/user/register',methods=['POST','GET'])
def add_user():
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        repeatpass = request.form.get("repeatpass")
        email = request.form.get("email")
        mobile = request.form.get("mobile")
        if name=='' or password=='':
	    return render_template('adduser.html')
        if password != repeatpass:
            return render_template('adduser.html')
        sql = "insert into users(name,password,email,mobile) values ('%s','%s','%s','%s')" % (name,password,email,mobile)
        cur.execute(sql)
        return redirect("/userlist")
    else:
        return render_template('adduser.html')

@app.route('/user/moduser',methods=['POST','GET'])
def mod_user():
    if request.method == "GET":
        id = request.args.get('id')
        fields = ['name','email','mobile']
        sql = "select %s from users where id=%d" % (','.join(fields),int(id))
        cur.execute(sql)
        res = cur.fetchone()
	user=dict(zip(fields,res))
        return render_template('modify.html',user=user)
    else:
	name = request.form.get("username")
	email = request.form.get("email")
	mobile = request.form.get("mobile")
	sql = "update users set email='%s',mobile='%s' where name='%s'" %(email,mobile,name)
	cur.execute(sql)
	return redirect("/userlist")

@app.route('/user/deluser')
def del_user():
    id = request.args.get('id')
    sql = "delete from users where id=%d" % int(id)
    cur.execute(sql)
    return redirect("/userlist")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)

