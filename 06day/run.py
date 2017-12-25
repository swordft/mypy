#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作业 用户管理（基于文件存储）

# 1. 管理员登录（写死账号是admin 密码是pwd）
# 2. 登录之后，看到用户和密码列表（存储在文件中），支持添加、删除、修改密码的操作

from flask import Flask,request,render_template,redirect
from api import getuserinfo,adduser,deluser,modpass,checkuser
import MySQLdb as mysql
app = Flask(__name__)

db = mysql.connect(user='root',passwd='xiaofang',db='reboot')
cur = db.cursor()

#@app.route('/')
#def admin():
#    return render_template('login.html')
#
#@app.route('/auth')
#def auth():
#    user = request.args.get('username')
#    pwd = request.args.get('password')
#    if user == "fangtao" and pwd == "xiaofang":
#        return redirect('/users')
#    else:
#        return "username or password is error!"
#
#            
#@app.route('/users')
#def user():
#    user_list = getuserinfo()
#    return render_template('users.html',ulist=user_list)
#
#@app.route('/adduser')
#def add_user():
#    name = request.args.get("username")
#    passwd = request.args.get("password")
#    if not checkuser(name,passwd):
#        return "user or password not null"
#    if name in getuserinfo():
#        return "user has already exist"
#    adduser(name,passwd)
#    return redirect("/users")
#
#@app.route('/deluser')
#def del_user():
#    name = request.args.get("username")
#    if name not in getuserinfo():
#        return "user does not exist!"
#    deluser(name)
#    return redirect("/users")
#
#@app.route('/modpass')
#def mod_pass():
#    name = request.args.get("username")
#    passwd = request.args.get("password")
#    if name not in getuserinfo():
#        return "user does not exist!"
#    deluser(name)
#    modpass(name,passwd)
#    return redirect("/users")

def deluser(name):
    sql = "delete from users where name=name"
    cur.execute(sql)
    return redirect("/users")

@app.route('/users')
def user():
    fields = ['name','name_cn','password','email','mobile']
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

@app.route('/getone')
def getone():
    id = request.args.get('id')
    fields = ['id','name','name_cn','email','mobile']
    sql = "select %s from users where id=%d" % (','.join(fields),int(id))
    cur.execute(sql)
    res = cur.fetchone()
    print res 
#@app.route('/deluser')
#def del_user():
#    sql = "delete from users where name=name"
#    cur.execute(sql)
#    return redirect("/users")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)

