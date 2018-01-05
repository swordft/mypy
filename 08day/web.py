#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
import time
import json
import traceback

app = Flask(__name__)

db = mysql.connect(user='root',passwd='xiaofang',db='reboot')
cur = db.cursor()

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        if not data.get('name',None) or not data.get('password',None):
            errmsg = "name or password not null"
            return render_template('login.html',error=errmsg)
        sql = "select name,password from users where name=%s" % data['name']
        cur.execute(sql)
        res = cur.fetchone()
        fields = ['name','password']
        user = {}
        user = dict((k,res[i]) for i,k in enumerate(fields))
        if not user['name'] == data['name'] or not user['password'] == data['password']:
            errmsg = "name or password is wrong"
            return render_template('login.html',error=errmsg)
    else:
        return render_template('login.html')








if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)
