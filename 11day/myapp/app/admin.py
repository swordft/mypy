#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
import MySQLdb as mysql
import time
import json
import traceback
import hashlib

app = Flask(__name__)
app.secret_key="1q2w3e4R"
salt = "aaaaa"

db = mysql.connect(user='root',passwd='xiaofang',db='reboot',unix_socket='/data/mysql/mysql.sock',charset='utf8')
#db = mysql.connect(user='root',passwd='xiaofang',db='reboot',unix_socket='/var/lib/mysql/mysql.sock',charset='utf8')
cur = db.cursor()

# 用户管理
@app.route('/')
@app.route('/login',methods=['POST','GET'])
def login():
    print "hello world!"
    # 用户第一次打开登录页面为GET请求，返回一个空的登录页
    if request.method == "GET":
        return render_template("login.html")
    # 如果用户点击按钮，提交POST请求，表明已经填写了用户名和密码，则获取表单的值，然后判断用户密码是否正确
    # 如果不正确则输出错误信息到前端jQuery，如果正确则创建session，并返回正确码code到前端jQuery
    if request.method == "POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        data['password'] = hashlib.md5(data['password']+salt).hexdigest()
        if not data.get('name',None) or not data.get('password',None):
            return json.dumps({'code':'1','errmsg':"name or password not null"})
        fields = ['name','password','role','status']
        sql = "select %s from users where name='%s'" % (','.join(fields),data['name'])
        cur.execute(sql)
        res = cur.fetchone()
        if not res:       #如果这个用户在数据库中不存在，返回的结果就是res=(())
            return json.dumps({'code':1,'errmsg':'user does not exists'})
        user = {}
        user = dict((k,res[i]) for i,k in enumerate(fields))
        if user['status'] == 1:
            return json.dumps({'code':'1','errmsg':'account is locked! please contact administrator'})
        elif user['password'] != data['password']:
            return json.dumps({'code':'1','errmsg':'password is wrong'})
        else:
            session['name'] = user['name']
            session['role'] = user['role']
            return json.dumps({'code':'0','errmsg':"login success"})

#@app.route('/index')
#def index():
#    if not session.get('name',None):
#        return redirect('/login')
#    return render_template("index.html",info=session)

@app.route('/logout')
def logout():
    if session.get('username'):
        session.pop('name',None)
        session.pop('role',None)
    else:
        return redirect('/login')

@app.route('/userlist')
def userlist():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    fields = ['id','name','name_cn','mobile','email','role','status']
    if role == "admin":
        sql = "select %s from users" % ','.join(fields)
    else:
        sql = "select %s from users where name='%s'" % (','.join(fields),name)
    cur.execute(sql)
    res = cur.fetchall()
    data = [dict((k,row[i]) for i,k in enumerate(fields)) for row in res]
    return render_template('userlist.html',users=data,info=session)

@app.route('/add_user',methods=['GET','POST'])
def add_user():
    if not session.get('name',None):
        return redirect('/login')
    if request.method == "GET":
        return render_template('add.html',info=session)
    if request.method == "POST":
	data = dict((k,v[0]) for k,v in dict(request.form).items())
        print "data=",data
        data['password'] = hashlib.md5(data['password']+salt).hexdigest()    # 对密码进行md5加密
        fields = ['name','name_cn','password','mobile','email','role','status']
        # 检查是否存在相同用户名
        sql = "SELECT COUNT(*) FROM users WHERE name='%s'" % data['name']
        cur.execute(sql)
        res = cur.fetchall()
        numbers = res[0][0]
        if numbers != 0:
            return json.dumps({'code':'1','errmsg':"username duplicate,please choice another!"})
        try:
	    sql = "INSERT INTO users (%s) VALUES (%s)" % (','.join(fields),','.join(["'%s'" % data[x] for x in fields]))
            cur.execute(sql)
            return json.dumps({'code':'0','errmsg':"add user success"})
        except Exception,e:
            errmsg = e
            return json.dumps({"code":'1',"errmsg":errmsg})

@app.route('/del_user')
def del_user():
    if not session.get('name',None):
        return redirect('/login')
    uid = request.args.get('id')
    sql = "delete from users where id=%s" % uid
    cur.execute(sql)
    return json.dumps({'code':'0','errmsg':"delete user success"})
    
@app.route('/update_user',methods=['GET','POST'])
def update():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    info = {'name':name,'role':role}
    #if request.method == 'GET':
    #    uid = request.args.get('id')
    #    return render_template('update.html',uid=uid,info=info)
    if request.method == 'POST':
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        if info['role'] == "admin":
            fields = ['id','name','name_cn','password','mobile','email','role','status']
        else:
            fields = ['id','name','name_cn','password','mobile','email']
        data = dict((f,data[f]) for f in fields)
        conditions = ["%s='%s'" % (k,v) for k,v in data.items()]
        try:
            sql = "update users set %s where id=%s" % (','.join(conditions),data['id'])
            cur.execute(sql)
            return json.dumps({"code":0,"errmsg":"update success"})
        except Exception,e:
	    errmsg = e
            return json.dumps({"code":1})

@app.route('/getbyid')
def getbyid():
    if not session.get('name',None):
        return redirect('/login')
    id = request.args.get('id')
    if not id:
        return json.dumps({"code":1,"errmsg":"must have a condition"})
    condition = 'id="%s"' % id
    fields = ['id','name','name_cn','password','email','mobile','role','status']
    try:
        sql = "select %s from users where %s" % (','.join(fields),condition)
        cur.execute(sql)
        res = cur.fetchone()
        user = {}
        user = dict((k,res[i]) for i,k in enumerate(fields))
        return json.dumps({"code":0,"result":user})
    except:
        return json.dumps({"code":1,"errmsg":"select userinfo failed"})

# 配置库管理
@app.route('/idc')
def idc():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    fields = ['id','name','city','address']
    sql = "select %s from idc" % ','.join(fields)
    cur.execute(sql)
    res = cur.fetchall()
    data = [dict((k,row[i]) for i,k in enumerate(fields)) for row in res]
    return render_template('idc.html',data=data,info=session)

@app.route('/cabinet')
def cabinet():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    fields = ['id','cicode','location','capacity','idc']
    sql = "select %s from cabinet" % ','.join(fields)
    cur.execute(sql)
    res = cur.fetchall()
    data = [dict((k,row[i]) for i,k in enumerate(fields)) for row in res]
    return render_template('cabinet.html',data=data,info=session)

@app.route('/server')
def server():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    fields = ['id','cicode','sn','model','architecture','cpu','memory','disk','cabinet','ip','hostname','os']
    sql = "select %s from server" % ','.join(fields)
    cur.execute(sql)
    res = cur.fetchall()
    data = [dict((k,row[i]) for i,k in enumerate(fields)) for row in res]
    return render_template('server.html',data=data,info=session)

@app.route('/update_server',methods=['GET','POST'])
def update_server():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    info = {'name':name,'role':role}
    if request.method == 'GET':
        id = request.args.get('id')
        return render_template('update_server.html',id=id,info=info)
    if request.method == 'POST':
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        if info['role'] == "admin":
            fields = ['id','name','name_cn','password','mobile','email','role','status']
        else:
            fields = ['id','name','name_cn','password','mobile','email']
        data = dict((f,data[f]) for f in fields)
        conditions = ["%s='%s'" % (k,v) for k,v in data.items()]
        try:
            sql = "update users set %s where id=%s" % (','.join(conditions),data['id'])
            cur.execute(sql)
            return json.dumps({"code":0,"errmsg":"update success"})
        except Exception,e:
	    errmsg = e
            return json.dumps({"code":1})

