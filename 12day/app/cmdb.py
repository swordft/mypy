#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
from . import app
import json
import traceback
from db import *

fields_cabinet = ['id','name','idc_id','u_num','power']
fields_idc = ['id','name','name_cn','address','admin','phone','num']

@app.route('/cabinet')
def cabinet():
    if not session.get('name'):
        return render_template('login.html')
    role = session.get('role')
    cabinets = get_list('cabinet',fields_cabinet)
    for i in cabinets:
        idc = get_list('idc',fields_idc,i['idc_id'])
        i['idc_id'] = idc['name']
    return render_template('cabinet.html',cabinets=cabinets,role=role)
