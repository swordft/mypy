#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
from . import app
import json
import traceback
from db import *

fields_cabinet = ['id','name','idc_id','u_num','power']
fields_idc = ['id','name','name_cn','address','admin','phone','num']

#@app.route('/cabinet')
#def cabinet():
#    if not session.get('name'):
#        return render_template('login.html')
#    role = session.get('role')
#    cabinets = get_list('cabinet',fields_cabinet)
#    for i in cabinets:
#        idc = get_list('idc',fields_idc,i['idc_id'])
#        i['idc_id'] = idc['name']
#    return render_template('cabinet.html',cabinets=cabinets,role=role)

@app.route('/idc')
def idc():
    if not session.get('name',None):
        return redirect('/login')
    name = session['name']
    role = session['role']
    fields = ['id','name','name_cn','address','admin','phone','num']
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
    fields = ['id','name','idc_id','u_num','power']
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
    fields = ['id','hostname','inter_ip','outer_ip','cabinet_id','op','phone']
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

