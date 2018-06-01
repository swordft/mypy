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
    idc_names = idcs.values()
    for cab in cabinets:
        if cab['idc_id'] in idcs:
            cab['idc_id'] = idcs[cab['idc_id']]
    return render_template('cabinet.html',idc_names=idc_names,idcs=idcs,data=cabinets,info=session)

@app.route('/server')
def server():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    servers = get_list('server',fields_server)
    cabinets = dict([(i['id'],i['name']) for i in get_list('cabinet',fields_cabinet)])
    cabinet_names = cabinets.values()
    for srv in servers:
        if srv['cabinet_id'] in cabinets:
            srv['cabinet_id'] = cabinets[srv['cabinet_id']]
    return render_template('server.html',cabinet_names=cabinet_names,cabinets=cabinets,data=servers,info=session)

# 添加配置项
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
        condition = 'name="%s"' % data['name']
        res = get_list('idc',fields_idc,condition)
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
        idcs = get_list('idc',fields_idc)
        return render_template('add_cabinet.html',idcs=idcs)
    if request.method == 'POST':
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        fields = ['name','idc_id','u_num','power']
        condition = 'name="%s"' % data['name']
        res = get_list('cabinet',fields,condition)
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
        cabinets = get_list('cabinet',fields_cabinet)
        return render_template('add_server.html',cabinets=cabinets)
    if request.method == 'POST':
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        fields = ['hostname','inter_ip','outer_ip','cabinet_id','op','phone']
        condition = 'hostname="%s"' % data['hostname']
        res = get_list('server',fields,condition)
        if res:
            return json.dumps({'code':'1','errmsg':"The name of server is duplicated,please choice another!"})
        try:
            insert('server',fields,data)
            return json.dumps({'code':'0','errmsg':"add server success"})
        except Exception,e:
            errmsg = e
            return json.dumps({"code":'1',"errmsg":errmsg})

# 删除配置项
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

# 更新配置项
@app.route('/update_idc',methods=['GET','POST'])
def update_idc():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    info = {'name':name,'role':role}
    if request.method == 'POST':
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        data = dict((f,data[f]) for f in fields_idc)
        conditions = ["%s='%s'" % (k,v) for k,v in data.items()]
        try:
            sql = "update %s set %s where id=%s" % ('idc',','.join(conditions),data['id'])
            cur.execute(sql)
            return json.dumps({"code":0,"errmsg":"update success"})
        except Exception,e:
	    errmsg = e
            return json.dumps({"code":1})

@app.route('/update_cabinet',methods=['GET','POST'])
def update_cabinet():
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
        data = dict((f,data[f]) for f in fields_cabinet)
        idcs = dict([(i['id'],i['name_cn']) for i in get_list('idc',fields_idc)])
        for i in idcs:
            if data['idc_id'] == idcs[i]:
                data['idc_id'] = i
        conditions = ["%s='%s'" % (k,v) for k,v in data.items()]
        try:
            sql = "update %s set %s where id=%s" % ('cabinet',','.join(conditions),data['id'])
            cur.execute(sql)
            return json.dumps({"code":0,"errmsg":"update success"})
        except Exception,e:
	    errmsg = e
            return json.dumps({"code":1})

@app.route('/update_server',methods=['GET','POST'])
def update_server():
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
        data = dict((f,data[f]) for f in fields_server)
        cabinets = dict([(i['id'],i['name']) for i in get_list('cabinet',fields_cabinet)])
        for i in cabinets:
            if data['cabinet_id'] == cabinets[i]:
                data['cabinet_id'] = i
        conditions = ["%s='%s'" % (k,v) for k,v in data.items()]
        try:
            sql = "update %s set %s where id=%s" % ('server',','.join(conditions),data['id'])
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
        data = get_list('idc',fields_idc,condition)
        return json.dumps({"code":0,"result":data})
    except:
        return json.dumps({"code":1,"errmsg":"select userinfo failed"})

@app.route('/cabinet_getbyid')
def cabinet_getbyid():
    if not session.get('name',None):
        return redirect('/login')
    id = request.args.get('id')
    if not id:
        return json.dumps({"code":1,"errmsg":"must have a condition"})
    condition = 'id="%s"' % id
    try:
        data = get_list('cabinet',fields_cabinet,condition)
        return json.dumps({"code":0,"result":data})
    except:
        return json.dumps({"code":1,"errmsg":"select userinfo failed"})

@app.route('/server_getbyid')
def server_getbyid():
    if not session.get('name',None):
        return redirect('/login')
    id = request.args.get('id')
    if not id:
        return json.dumps({"code":1,"errmsg":"must have a condition"})
    condition = 'id="%s"' % id
    try:
        data = get_list('server',fields_server,condition) 
        return json.dumps({"code":0,"result":data})
    except:
        return json.dumps({"code":1,"errmsg":"select userinfo failed"})

