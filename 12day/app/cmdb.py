#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
from . import app
import MySQLdb as mysql
import json
import traceback
from db import *

fields_cabinet = ['id','name','idc_id','u_num','power']
fields_idc = ['id','name','name_cn','address','admin','phone','num']
fields_server = ['id','hostname','inter_ip','outer_ip','cabinet_id','op','phone']

@app.route('/idc')
def idc():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    idcs = get_list('idc',fields_idc)
    return render_template('idc.html',data=idcs,info=session)

@app.route('/cabinet')
def cabinet():
    if not session.get('name'):
        return render_template('login.html')
    name = session['name']
    role = session.get('role')
    cabinets = get_list('cabinet',fields_cabinet)
    idcs = dict([(i['id'],i['name_cn']) for i in get_list('idc',fields_idc)])
    for cab in cabinets:
        if cab['idc_id'] in idcs:
            cab['idc_id'] = idcs[cab['idc_id']]
    return render_template('cabinet.html',data=cabinets,info=session)

@app.route('/server')
def server():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    servers = get_list('server',fields_server)
    cabinets = dict([(i['id'],i['name']) for i in get_list('cabinet',fields_cabinet)])
    print "cabinets=",cabinets
    print "servers=",servers
    for srv in servers:
        if srv['cabinet_id'] in cabinets:
            srv['cabinet_id'] = cabinets[srv['cabinet_id']]
    return render_template('server.html',data=servers,info=session)

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

@app.route('/add_idc',methods=['GET','POST'])
def add_idc():
    if not session.get('name',None):
        return redirect('/login')
    if request.method == 'GET':
        id = request.args.get('id')
        return render_template('add_idc.html')
    if request.method == 'POST':
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        fields = ['name','name_cn','address','admin','phone','num']
        res = get_list('idc',fields_idc,data['name'])
        if res:
            return json.dumps({'code':'1','errmsg':"The name of idc is duplicated,please choice another!"})
        try:
            insert('idc',fields,data)
            return json.dumps({'code':'0','errmsg':"add idc success"})
        except Exception,e:
            errmsg = e
            return json.dumps({"code":'1',"errmsg":errmsg})
 
@app.route('/add_cabinet',methods=['GET','POST'])
def add_cabinet():
    if not session.get('name',None):
        return redirect('/login')
    if request.method == 'GET':
        id = request.args.get('id')
        return render_template('add_cabinet.html')
    if request.method == 'POST':
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        fields = ['name','idc_id','u_num','power']
        res = get_list('cabinet',fields,data['name'])
        if res:
            return json.dumps({'code':'1','errmsg':"The name of cabinet is duplicated,please choice another!"})
        try:
            insert('cabinet',fields,data)
            return json.dumps({'code':'0','errmsg':"add cabinet success"})
        except Exception,e:
            errmsg = e
            return json.dumps({"code":'1',"errmsg":errmsg})


@app.route('/add_server',methods=['GET','POST'])
def add_server():
    if not session.get('name',None):
        return redirect('/login')
    if request.method == 'GET':
        id = request.args.get('id')
        return render_template('add_server.html')
    if request.method == 'POST':
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        fields = ['hostname','inter_ip','outer_ip','cabinet_id','op','phone']
        res = get_list('server',fields,data['hostname'])
        if res:
            return json.dumps({'code':'1','errmsg':"The name of server is duplicated,please choice another!"})
        try:
            insert('server',fields,data)
            return json.dumps({'code':'0','errmsg':"add server success"})
        except Exception,e:
            errmsg = e
            return json.dumps({"code":'1',"errmsg":errmsg})


@app.route('/del_idc')
def del_idc():
    if not session.get('name',None):
        return redirect('/login')
    id = request.args.get('id')
    try:
        delete('idc','id',id)
        return json.dumps({'code':'0','errmsg':"delete idc success"})
    except Exception,e:
        errmsg = e
        return json.dumps({'code':1,'errmsg':'delete idc failed!'})

@app.route('/del_cabinet')
def del_cabinet():
    if not session.get('name',None):
        return redirect('/login')
    id = request.args.get('id')
    try:
        delete('cabinet','id',id)
        return json.dumps({'code':'0','errmsg':"delete cabinet success"})
    except Exception,e:
        errmsg = e
        return json.dumps({'code':1,'errmsg':'delete cabinet failed!'})

@app.route('/del_server')
def del_server():
    if not session.get('name',None):
        return redirect('/login')
    id = request.args.get('id')
    try:
        delete('server','id',id)
        return json.dumps({'code':'0','errmsg':"delete server success"})
    except Exception,e:
        errmsg = e
        return json.dumps({'code':1,'errmsg':'delete server failed!'})

@app.route('/update_idc',methods=['GET','POST'])
def update_idc():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    info = {'name':name,'role':role}
    if request.method == 'POST':
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        #if info['role'] == "admin":
        #    fields = ['id','name','name_cn','address','admin','phone','num'] 
        #else:
        #    fields = ['id','name','name_cn','password','mobile','email']
        data = dict((f,data[f]) for f in fields_idc)
        conditions = ["%s='%s'" % (k,v) for k,v in data.items()]
        try:
            sql = "update %s set %s where id=%s" % ('idc',','.join(conditions),data['id'])
            print "sql=",sql
            cur.execute(sql)
            return json.dumps({"code":0,"errmsg":"update success"})
        except Exception,e:
	    errmsg = e
            return json.dumps({"code":1})

@app.route('/idc_getbyid')
def idc_getbyid():
    if not session.get('name',None):
        return redirect('/login')
    id = request.args.get('id')
    if not id:
        return json.dumps({"code":1,"errmsg":"must have a condition"})
    condition = 'id="%s"' % id
    try:
        sql = "select %s from idc where %s" % (','.join(fields_idc),condition)
        cur.execute(sql)
        res = cur.fetchone()
        data = {}
        data = dict((k,res[i]) for i,k in enumerate(fields_idc))
        return json.dumps({"code":0,"result":data})
    except:
        return json.dumps({"code":1,"errmsg":"select userinfo failed"})

