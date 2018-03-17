#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 注册，即添加用户，第一次请求获取注册页面，用GET请求，点击表单按钮提交用post方式，执行sql插入数据，注册成功
# 则跳转到个人信息页面，失败则在注册页面打印错误信息
# 思路：
# 1.前端：做一个注册html页面，里面写好表单，表单的action对应逻辑端的register方法，请求方式method为post
# 2.逻辑端：get请求直接render_template("register.html")，返回空表单，提供填写接口，点击表单按钮时，提交的是POST方式，获取表单
# 的内容，并将内容插入到数据库
# 3.数据端：接受逻辑端的SQL请求，将数据写入数据库

# 功能：
# 1. 任何操作都必须先登录，然后通过session记住登录状态
# 2. 每个操作都会对状态进行判断，登录状态的情况下才会执行动作，否则跳转到登录页面
# 3. 完整的用户管理的应用场景和技术上完整增删改查

# 用户权限管理系统业务逻辑思路
# 1. 第一步让用户登录，已登录的状态会有session记录
# 2. 判断用户是否存在
# 3.1 如果用户不存在，会提示，需要管理员创建用户（运维内部系统，不建议自由注册）
# 3.2 如果用户存在且登录成功，生成session记录用户状态，然后跳转到用户个人信息页面，用户可以修改自己的一部分信息
# 4. 用户列表页面，只有管理员才有资格看到，能够对所有用户增删改查，增删改查的每个函数都要从session中取出用户的角色，判断是否为管理员角色
from flask import Flask,request,render_template,redirect,session
from models import *
import MySQLdb as mysql
import time
import json
import traceback

app = Flask(__name__)
app.secret_key="1q2w3e4R"
#db = mysql.connect(user='root',passwd='xiaofang',db='reboot')
#cur = db.cursor()

@app.route('/')
def index():
    if not session.get('name',None):
        return redirect('/login')
    else:
        return redirect('/userlist')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        #data = {}
        #data["name"] = request.form.get('name',None)
        #data["name_cn"] = request.form.get('name_cn',None)
        #data["mobile"] = request.form.get('mobile',None)
        #data["email"] = request.form.get('email',None)
        #data["role"] = request.form.get('role',None)
        #data["status"] = request.form.get('status',None)
	#data["password"] = request.form.get('password',None)
        #data["repwd"] = request.form.get('repwd',None)
	#data["create_time"] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	data = dict((k,v[0]) for k,v in dict(request.form).items())
	data["create_time"] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

        # fields,values = [],[]
	# for k,v in data.items():
	#     fields.append(k)
	#     values.append(v)
	if not data["name"] or not data["password"] or not data["role"]:
            errmsg = "name or password or role not null"
	    return render_template("register.html",error=errmsg)
	    
	if data["password"] != data["repwd"]:
	    errmsg = "The two passwords you typed do not match!"
	    return render_template("register.html",error=errmsg)
	fields = ['name','name_cn','password','mobile','email','role','status','create_time']
        values = ','.join(["'%s'" % data[x] for x in fields]) 
        fields = ','.join(fields)
	try:
	    #sql = "INSERT INTO users (%s) VALUES (%s)" % (','.join(fields),','.join(["'%s'" % data[x] for x in fields]))
	    #cur.execute(sql)
            add_user(fields,values)
            #return redirect("/userinfo?name=%s" % data['name'])
            return redirect("/login")
        except Exception,e:
	    errmsg = e
	    return render_template("register.html",error=errmsg)
    else:
        return render_template("register.html")

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        #username = request.form.get('username',None)
	#password = request.form.get('password',None)
        userinfo = dict((k,v[0]) for k,v in dict(request.form).items())
	if not userinfo.get('name',None) or not userinfo.get('password',None):
	    errmsg = "must have a name and password"
	    return render_template("login.html",error=errmsg)
        fields = ['id','name','password','role','status']
        res = check_user(fields,'name',userinfo['name'])
	if not res:
            errmsg = "username does not exists"
            return render_template("login.html",error=errmsg)
        res = dict((k,res[i]) for i,k in enumerate(fields))
	#sql = "select name,password from users where name='%s'" % userinfo['username']
	#cur.execute(sql)
	#res = cur.fetchone()
	if userinfo['password'] == res['password']:
            if res['status'] != 'Normal':
                errmsg = "account locked,please contact your administrator"
	        return render_template("login.html",error=errmsg)
            session['id'] = res['id']
            session['name'] = res['name']
            session['role'] = res['role']
            print "session=",session
            return redirect("/userlist")
	else:
            errmsg = "password error"
            return render_template("login.html",error=errmsg)
    else:
	return render_template("login.html")


@app.route('/userlist')
def userlist():
    users = []
    fields = ['id','name','name_cn','email','mobile','role','status']
    id = (session['id'],)
    try:
        if session['role'] == 'admin':
            res = get_userlist(fields)
        else:
            res = get_userlist(fields,*id)
    #    res = get_userlist(fields)
	#sql = "select %s from users" % ','.join(fields)
	#cur.execute(sql)
	#res = cur.fetchall()
	##for row in res:
        ##    user = {}
	##    for i,k in enumerate(fields):
	##        user[k] = row[i]
	##    users.append(user)
        users = [dict((k,row[i]) for i,k in enumerate(fields)) for row in res]
        return render_template('userlist.html',users=users,role=session['role'])
    except Exception,e:
	errmsg = e
	return render_template('userlist.html',error=errmsg)

@app.route('/delete')
def delete():
    id = request.args.get('id',None)
    try:
        del_user(id)
	#sql = "delete from users where id=%s" % id
	#cur.execute(sql)
	return redirect('/userlist')
    except Exception,e:
	errmsg = e
	return render_template('userlist.html',error=errmsg)
	
@app.route('/update',methods=['GET','POST'])
def update():
    if request.method == 'GET':
	id = request.args.get('id',None)
	if not id:
	    errmsg = "must have id"
	    return render_template("update.html",error=errmsg)
        fields = ['id','name','name_cn','email','mobile','role','password']
	try:
	    #sql = "select %s from users where id=%s" % (','.join(fields),id)
	    #cur.execute(sql)
	    #res = cur.fetchone()
            res = check_user(fields,'id',id)
	    user = dict((k,res[i]) for i,k in enumerate(fields))
	    return render_template('update.html',user=user,role=session['role'])
        except Exception,e:
	    errmsg = e
	    return render_template('update.html',error=errmsg)
    else:
	user = dict((k,v[0]) for k,v in dict(request.form).items())
        if user['password'] != user['repwd']:
            errmsg = "repeat password not matched"
	    return render_template("update.html",error=errmsg)
	conditions = ','.join(["%s='%s'" % (k,v) for k,v in user.items() if k != "repwd"])
        #user = {}
	#user["id"] = request.form.get('id',None)
        #user["name"] = request.form.get('name',None)
        #user["name_cn"] = request.form.get('name_cn',None)
        #user["mobile"] = request.form.get('mobile',None)
        #user["email"] = request.form.get('email',None)
        #user["role"] = request.form.get('role',None)
        #user["status"] = request.form.get('status',None)
	try:
	    #sql = "update users set %s where id=%s" % (','.join(["%s='%s'" %(k,v) for k,v in user.items()]),user["id"])
	    #sql = "update users set %s where id=%s" % (conditions,user['id'])
	    #cur.execute(sql)
            update_user(conditions,user['id']) 
	    return redirect('/userlist')
        except Exception,e:
	    errmsg = e
	    return render_template('update.html',error=errmsg)
	    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9090,debug=True)
