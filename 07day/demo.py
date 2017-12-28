#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 注册，即添加用户，第一次请求获取注册页面，用GET请求，点击表单按钮提交用post方式，执行sql插入数据，注册成功
# 则跳转到个人信息页面，失败则在注册页面打印错误信息
# 思路：
# 1.前端：做一个注册html页面，里面写好表单，表单的action对应逻辑端的register方法，请求方式method为post
# 2.逻辑端：get请求直接render_template("register.html")，返回空表单，提供填写接口，点击表单按钮时，提交的是POST方式，获取表单
# 的内容，并将内容插入到数据库
# 3.数据端：接受逻辑端的SQL请求，将数据写入数据库
from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
import time

app = Flask(__name__)

db = mysql.connect(user='root',passwd='xiaofang',db='reboot')
cur = db.cursor()

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data = {}
        data["name"] = request.form.get('name',None)
        data["name_cn"] = request.form.get('name_cn',None)
        data["mobile"] = request.form.get('mobile',None)
        data["email"] = request.form.get('email',None)
        data["role"] = request.form.get('role',None)
        data["status"] = request.form.get('status',None)
	data["password"] = request.form.get('password',None)
        data["repwd"] = request.form.get('repwd',None)
	data["create_time"] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

	fields = ['name','name_cn','password','mobile','email','role','status','create_time']
	if not data["name"] or not data["password"] or not data["role"]:
            errmsg = "name or password or role not null"
	    return render_template("register.html",error=errmsg)
	    
	if data["password"] != data["repwd"]:
	    errmsg = "The two passwords you typed do not match!"
	    return render_template("register.html",error=errmsg)
	try:
	    sql = "INSERT INTO users (%s) VALUES (%s)" % (','.join(fields),','.join(["'%s'" % data[x] for x in fields]))
	    cur.execute(sql)
            return render_template("login.html")
	except:
	    errmsg = "insert failed"
	    return render_template("register.html",error=errmsg)
    else:
        return render_template("register.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9090,debug=True)
