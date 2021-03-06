#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作业 用户管理（基于文件存储）

# 1. 管理员登录（写死账号是admin 密码是pwd）
# 2. 登录之后，看到用户和密码列表（存储在文件中），支持添加、删除、修改密码的操作

from flask import Flask,request,render_template,redirect
from api import getuserinfo,adduser,deluser,modpass,checkuser
app = Flask(__name__)


@app.route('/')
def admin():
    return render_template('login.html')

@app.route('/auth')
def auth():
    user = request.args.get('username')
    pwd = request.args.get('password')
    if user == "fangtao" and pwd == "xiaofang":
        return redirect('/users')
    else:
        return "username or password is error!"

            
@app.route('/users')
def user():
    user_list = getuserinfo()
    return render_template('users.html',ulist=user_list)

@app.route('/adduser')
def add_user():
    name = request.args.get("username")
    passwd = request.args.get("password")
    if not checkuser(name,passwd):
        return "user or password not null"
    if name in getuserinfo():
        return "user has already exist"
    adduser(name,passwd)
    return redirect("/users")

@app.route('/deluser')
def del_user():
    name = request.args.get("username")
    if name not in getuserinfo():
        return "user does not exist!"
    deluser(name)
    return redirect("/users")

@app.route('/modpass')
def mod_pass():
    name = request.args.get("username")
    passwd = request.args.get("password")
    if name not in getuserinfo():
        return "user does not exist!"
    deluser(name)
    modpass(name,passwd)
    return redirect("/users")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)

