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

# 常用的动作
# $(选择器).html(value)     获取或设置html标签值
# $(选择器).val(value)     获取或设置表单标签值
# $(选择器).attr(value)     获取或设置属性标签值
# $(选择器).css(value)     获取或设置标签样式值

# 1. id选择器和class选择器是最常用的两种选择器
# 2. id选择器的id在页面是唯一的标识，适用于某一个特定元素的定义
# 3. class选择器，是同一类元素共用属性，适用于相同类型元素批量的定义

# 更新第一步：
# 1. get请求，返回一空的表单html，我们需要通过ajax的getjson请求getbyid这个逻辑端拿到数据，然后将数据渲染到这个空表单中
# 2. post请求，ajax的post请求，逻辑端返回json串

# 美化页面
# 1. 将源文件中引用的静态文件全部按照源站的路径创建下载
# 2. 有选择的拷贝代码
# 3. 把自己的业务逻辑替换进来

# 作业：
# 1. 完成ajax对用户添加、更新、删除的操作
# 2. 套一套漂亮的界面

from flask import Flask,request,render_template,redirect,session
import MySQLdb as mysql
import time
import json
import traceback

app = Flask(__name__)
app.secret_key="1q2w3e4R"

db = mysql.connect(user='root',passwd='xiaofang',db='reboot',unix_socket='/data/mysql/mysql.sock')
#db = mysql.connect(user='root',passwd='xiaofang',db='reboot',unix_socket='/var/lib/mysql/mysql.sock')
cur = db.cursor()

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
	print "data=",data
        if not data.get('name',None) or not data.get('password',None):
            errmsg = "name or password not null"
            #return render_template('new_login.html',error=errmsg)
            return json.dumps({'code':'1','error':errmsg})
        fields = ['name','password','role']
        sql = "select %s from users where name='%s'" % (','.join(fields),data['name'])
        cur.execute(sql)
        res = cur.fetchone()
        if not res:       #如果这个用户在数据库中不存在，返回的结果就是res=(())
            errmsg = "%s is not exist" % data['name']
            return json.dumps({'code':1,'error':errmsg})
            #return render_template('new_login.html',error=errmsg)
        user = {}
        user = dict((k,res[i]) for i,k in enumerate(fields))
        if user['password'] != data['password']:
            errmsg = "password is wrong"
            return json.dumps({'code':'1','error':errmsg})
            #return render_template('new_login.html',error=errmsg)
        else:
            session['name'] = user['name']
            session['role'] = user['role']
            #return redirect('/userlist')
            return json.dumps({'code':'0','error':"login success"})
    else:
        return render_template('new_login.html')

@app.route('/userlist')
def userlist():
    if not session.get('name',None):
        return redirect('/login')
    return render_template('new_userlist.html')

@app.route('/get_userlist')
def get_userlist():
    if not session.get('name',None):
        return redirect('/login')
    users = []
    fields = ['id','name','name_cn','email','mobile','status','role']
    try:
	sql = "select %s from users" % ','.join(fields)
	cur.execute(sql)
	res = cur.fetchall()
	users = [dict((k,row[i]) for i,k in enumerate(fields)) for row in res]
        #return render_template('new_userlist.html',users=users)
        return json.dumps({'code':'0','result':users})
    except Exception,e:
	errmsg = e
	#return render_template('new_userlist.html',error=errmsg)
        return json.dumps({'code':'1'})

@app.route('/logout')
def logout():
    session.pop('name')
    return redirect('/login')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == "POST":
	data = dict((k,v[0]) for k,v in dict(request.form).items())
        fields = ['name','password','mobile','email','role']
        try:
	    sql = "INSERT INTO users (%s) VALUES (%s)" % (','.join(fields),','.join(["'%s'" % data[x] for x in fields]))
            cur.execute(sql)
            return json.dumps({'code':'0','errmsg':"update success"})
        except Exception,e:
	    errmsg = e
            return json.dumps({"code":'1',"errmsg":errmsg})

    else:
        return render_template('new_register.html')

@app.route('/update',methods=['GET','POST'])
def update():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    info = {'name':name,'role':role}
    if request.method == 'POST':
        data = dict(request.form)
        data = dict((k,v[0]) for k,v in data.items())
        fields = ['id','name','password','mobile','email','role']
        data = dict((f,data[f]) for f in fields)
        conditions = ["%s='%s'" % (k,v) for k,v in data.items()]
        try:
            sql = "update users set %s where id=%s" % (','.join(conditions),data['id'])
            cur.execute(sql)
            return json.dumps({"code":0,"result":"update success"})
        except Exception,e:
	    errmsg = e
            return json.dumps({"code":1})
	
    else:
        uid = request.args.get('id')
        return render_template('new_update.html',uid=uid,info=info)

@app.route('/getbyid')
def getbyid():
    if not session.get('name',None):
        return redirect('/login')
    id = request.args.get('id')
    if not id:
        return json.dumps({"code":1,"errmsg":"must have a condition"})
    condition = 'id="%s"' % id
    fields = ['id','name','password','email','mobile','role','status']
    try:
        sql = "select %s from users where %s" % (','.join(fields),condition)
        cur.execute(sql)
        res = cur.fetchone()
        user = {}
        user = dict((k,res[i]) for i,k in enumerate(fields))
        return json.dumps({"code":0,"result":user})
    except:
        return json.dumps({"code":1,"errmsg":"select userinfo failed"})

@app.route('/delete')
def delete():
    if not session.get('name',None):
        return redirect('/login')
    role = session['role']
    if role != 'admin':
        return json.dumps({'code':1,'errmsg':"you are not admin,no privilege"})
    id = request.args.get('id',None)
    if not id:
        errmsg = "must have id"
        return render_template("new_userlist.html",result=errmsg)
    try:
        sql = "delete from users where id=%s" % id
        cur.execute(sql)
	errmsg = "delete success"
        return render_template("new_userlist.html",result=errmsg)
        #return json.dumps({"code":0,"result":errmsg})
    except:
        errmsg = "delete failed"
        return json.dumps({"code":1,"result":errmsg})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)
