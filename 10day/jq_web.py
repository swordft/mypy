#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
import MySQLdb as mysql
import time
import json
import traceback

app = Flask(__name__)
app.secret_key="1q2w3e4R"

db = mysql.connect(user='root',passwd='xiaofang',db='reboot',unix_socket='/data/mysql/mysql.sock',charset='utf8')
#db = mysql.connect(user='root',passwd='xiaofang',db='reboot',unix_socket='/var/lib/mysql/mysql.sock')
cur = db.cursor()

@app.route('/')
@app.route('/login',methods=['POST','GET'])
def login():
    # 用户第一次打开登录页面为GET请求，返回一个空的登录页
    if request.method == "GET":
        return render_template("login.html")
    # 如果用户点击按钮，提交POST请求，表明已经填写了用户名和密码，则获取表单的值，然后判断用户密码是否正确
    # 如果不正确则输出错误信息到前端jQuery，如果正确则创建session，并返回正确码code到前端jQuery
    if request.method == "POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        if not data.get('name',None) or not data.get('password',None):
            return json.dumps({'code':'1','errmsg':"name or password not null"})
        fields = ['name','password','role']
        sql = "select %s from users where name='%s'" % (','.join(fields),data['name'])
        cur.execute(sql)
        res = cur.fetchone()
        if not res:       #如果这个用户在数据库中不存在，返回的结果就是res=(())
            return json.dumps({'code':1,'errmsg':'user does not exists'})
        user = {}
        user = dict((k,res[i]) for i,k in enumerate(fields))
        if user['password'] != data['password']:
            return json.dumps({'code':'1','errmsg':'password is wrong'})
        else:
            session['name'] = user['name']
            session['role'] = user['role']
            return json.dumps({'code':'0','errmsg':"login success"})

@app.route('/index')
def index():
    if not session.get('name',None):
        return redirect('/login')
    return render_template("index.html",info=session)

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
    fields = ['id','name','name_cn','mobile','email','role','status']
    sql = "select %s from users" % ','.join(fields)
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
        fields = ['name','name_cn','password','mobile','email','role','status']
	sql = "INSERT INTO users (%s) VALUES (%s)" % (','.join(fields),','.join(["'%s'" % data[x] for x in fields]))
        cur.execute(sql)
        return json.dumps({'code':'0','errmsg':"add user success"})

@app.route('/del_user')
def del_user():
    if not session.get('name',None):
        return redirect('/login')
    uid = request.args.get('id')
    sql = "delete from users where id=%s" % uid
    print "sql=",sql
    cur.execute(sql)
    return json.dumps({'code':0,'errmsg':"delete user success"})
    

#@app.route('/')
#def index():
#    return redirect('/login')
#
#@app.route('/login',methods=['POST','GET'])
#def login():
#    if request.method == "POST":
#        data = dict((k,v[0]) for k,v in dict(request.form).items())
#	print "data=",data
#        if not data.get('name',None) or not data.get('password',None):
#            errmsg = "name or password not null"
#            #return render_template('new_login.html',error=errmsg)
#            return json.dumps({'code':'1','error':errmsg})
#        fields = ['name','password','role']
#        sql = "select %s from users where name='%s'" % (','.join(fields),data['name'])
#        cur.execute(sql)
#        res = cur.fetchone()
#        if not res:       #如果这个用户在数据库中不存在，返回的结果就是res=(())
#            errmsg = "%s is not exist" % data['name']
#            return json.dumps({'code':1,'error':errmsg})
#            #return render_template('new_login.html',error=errmsg)
#        user = {}
#        user = dict((k,res[i]) for i,k in enumerate(fields))
#        if user['password'] != data['password']:
#            errmsg = "password is wrong"
#            return json.dumps({'code':'1','error':errmsg})
#            #return render_template('new_login.html',error=errmsg)
#        else:
#            session['name'] = user['name']
#            session['role'] = user['role']
#            #return redirect('/userlist')
#            return json.dumps({'code':'0','error':"login success"})
#    else:
#        return render_template('new_login.html')
#
#@app.route('/userlist')
#def userlist():
#    if not session.get('name',None):
#        return redirect('/login')
#    return render_template('new_userlist.html')
#
#@app.route('/get_userlist')
#def get_userlist():
#    if not session.get('name',None):
#        return redirect('/login')
#    users = []
#    fields = ['id','name','name_cn','email','mobile','status','role']
#    try:
#	sql = "select %s from users" % ','.join(fields)
#	cur.execute(sql)
#	res = cur.fetchall()
#	users = [dict((k,row[i]) for i,k in enumerate(fields)) for row in res]
#        #return render_template('new_userlist.html',users=users)
#        return json.dumps({'code':'0','result':users})
#    except Exception,e:
#	errmsg = e
#	#return render_template('new_userlist.html',error=errmsg)
#        return json.dumps({'code':'1'})
#
#@app.route('/logout')
#def logout():
#    session.pop('name')
#    return redirect('/login')
#
#@app.route('/register',methods=['GET','POST'])
#def register():
#    if request.method == "POST":
#	data = dict((k,v[0]) for k,v in dict(request.form).items())
#        fields = ['name','password','mobile','email','role']
#        try:
#	    sql = "INSERT INTO users (%s) VALUES (%s)" % (','.join(fields),','.join(["'%s'" % data[x] for x in fields]))
#            cur.execute(sql)
#            return json.dumps({'code':'0','errmsg':"update success"})
#        except Exception,e:
#	    errmsg = e
#            return json.dumps({"code":'1',"errmsg":errmsg})
#
#    else:
#        return render_template('new_register.html')
#
#@app.route('/update',methods=['GET','POST'])
#def update():
#    if not session.get('name',None):
#        return redirect('/login')
#    name = session['name']
#    role = session['role']
#    info = {'name':name,'role':role}
#    if request.method == 'POST':
#        data = dict(request.form)
#        data = dict((k,v[0]) for k,v in data.items())
#        fields = ['id','name','password','mobile','email','role']
#        data = dict((f,data[f]) for f in fields)
#        conditions = ["%s='%s'" % (k,v) for k,v in data.items()]
#        try:
#            sql = "update users set %s where id=%s" % (','.join(conditions),data['id'])
#            cur.execute(sql)
#            return json.dumps({"code":0,"result":"update success"})
#        except Exception,e:
#	    errmsg = e
#            return json.dumps({"code":1})
#	
#    else:
#        uid = request.args.get('id')
#        return render_template('new_update.html',uid=uid,info=info)
#
#@app.route('/getbyid')
#def getbyid():
#    if not session.get('name',None):
#        return redirect('/login')
#    id = request.args.get('id')
#    if not id:
#        return json.dumps({"code":1,"errmsg":"must have a condition"})
#    condition = 'id="%s"' % id
#    fields = ['id','name','password','email','mobile','role','status']
#    try:
#        sql = "select %s from users where %s" % (','.join(fields),condition)
#        cur.execute(sql)
#        res = cur.fetchone()
#        user = {}
#        user = dict((k,res[i]) for i,k in enumerate(fields))
#        return json.dumps({"code":0,"result":user})
#    except:
#        return json.dumps({"code":1,"errmsg":"select userinfo failed"})
#
#@app.route('/delete')
#def delete():
#    if not session.get('name',None):
#        return redirect('/login')
#    role = session['role']
#    if role != 'admin':
#        return json.dumps({'code':1,'errmsg':"you are not admin,no privilege"})
#    id = request.args.get('id',None)
#    if not id:
#        errmsg = "must have id"
#        return render_template("new_userlist.html",result=errmsg)
#    try:
#        sql = "delete from users where id=%s" % id
#        cur.execute(sql)
#	errmsg = "delete success"
#        return render_template("new_userlist.html",result=errmsg)
#        #return json.dumps({"code":0,"result":errmsg})
#    except:
#        errmsg = "delete failed"
#        return json.dumps({"code":1,"result":errmsg})
#
#
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)
