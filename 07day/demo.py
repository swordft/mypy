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
import json
import traceback

app = Flask(__name__)

db = mysql.connect(user='root',passwd='xiaofang',db='reboot')
cur = db.cursor()

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
	data = dict(request.form)
	data["create_time"] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	print "data=",data

        # fields,values = [],[]
	# for k,v in data.items():
	#     fields.append(k)
	#     values.append(v)
	fields = ['name','name_cn','password','mobile','email','role','status','create_time']
	if not data["name"][0] or not data["password"][0] or not data["role"][0]:
            errmsg = "name or password or role not null"
	    return render_template("register.html",error=errmsg)
	    
	if data["password"][0] != data["repwd"][0]:
	    errmsg = "The two passwords you typed do not match!"
	    return render_template("register.html",error=errmsg)
	try:
	    sql = "INSERT INTO users (%s) VALUES (%s)" % (','.join(fields),','.join(["'%s'" % data[x][0] for x in fields]))
	    cur.execute(sql)
            return redirect("/userinfo?name=%s" % data['name'][0])
        except Exception,e:
	    errmsg = e
	    return render_template("register.html",error=errmsg)
    else:
        return render_template("register.html")

@app.route('/userinfo')
def userinfo():
    where = {}
    where['id'] = request.args.get('id',None)
    where['name'] = request.args.get('name',None)
    if not where['id'] and not where['name']:
        errmsg = "must have a where"
	return render_template("index.html",error=errmsg)
    if where['id'] and not where['name']:
	condition = 'id = "%(id)s"' % where
    if where['name'] and not where['id']:
	condition = 'name = "%(name)s"' % where
    fields = ['id','name','name_cn','email','mobile']
    try:
	sql = "select %s from users where %s" %(','.join(fields),condition)
	cur.execute(sql)
	res = cur.fetchone()
	#user = {}
	#for i,k in enumerate(fields):
	#    user[k] = res[i]
	user = dict((k,res[i]) for i,k in enumerate(fields))
	return render_template("index.html",user=user)
    except Exception,e:
	errmsg = e
	return render_template("index.html",error=errmsg)

@app.route('/userlist')
def userlist():
    users = []
    fields = ['id','name','name_cn','email','mobile']
    try:
	sql = "select %s from users" % ','.join(fields)
	cur.execute(sql)
	res = cur.fetchall()
	#for row in res:
        #    user = {}
	#    for i,k in enumerate(fields):
	#        user[k] = row[i]
	#    users.append(user)
	users = [dict((k,row[i]) for i,k in enumerate(fields)) for row in res]
        return render_template('userlist.html',users=users)
    except Exception,e:
	errmsg = e
	return render_template('userlist.html',error=errmsg)

@app.route('/delete')
def delete():
    id = request.args.get('id',None)
    try:
	sql = "delete from users where id=%s" % id
	cur.execute(sql)
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
        fields = ['id','name','name_cn','email','mobile']
	try:
	    sql = "select %s from users where id=%s" % (','.join(fields),id)
	    cur.execute(sql)
	    res = cur.fetchone()
	    user = dict((k,res[i]) for i,k in enumerate(fields))
	    return render_template('update.html',user=user)
        except Exception,e:
	    errmsg = e
	    return render_template('update.html',error=errmsg)
    else:
	user = dict(request.form)
	conditions = ["%s='%s'" % (k,v[0]) for k,v in user.items()]
        #user = {}
	#user["id"] = request.form.get('id',None)
        #user["name"] = request.form.get('name',None)
        #user["name_cn"] = request.form.get('name_cn',None)
        #user["mobile"] = request.form.get('mobile',None)
        #user["email"] = request.form.get('email',None)
        #user["role"] = request.form.get('role',None)
        #user["status"] = request.form.get('status',None)
	try:
	    #sql = "update users set %s where id=%d" % (','.join(["%s='%s'" %(k,v) for k,v in user.items()]),int(user["id"]))
	    sql = "update users set %s where id=%s" % (','.join(conditions),user['id'][0])
	    cur.execute(sql)
	    return redirect('/userlist')
        except Exception,e:
	    errmsg = e
	    return render_template('update.html',error=errmsg)
	    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9090,debug=True)
