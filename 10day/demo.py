#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
import MySQLdb as mysql
import time
import json
import traceback

app = Flask(__name__)
#app.secret_key="1q2w3e4R"

#db = mysql.connect(user='root',passwd='xiaofang',db='reboot',unix_socket='/data/mysql/mysql.sock')
#db = mysql.connect(user='root',passwd='xiaofang',db='reboot',unix_socket='/var/lib/mysql/mysql.sock')
#cur = db.cursor()

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/userlist')
def userlist():
    user = {"name":"wd"}
    return render_template("userlist.html",user=user)

@app.route('/idc')
def idc():
    return render_template("idc.html")

@app.route('/cabinet')
def cabinet():
    return render_template("cabinet.html")

@app.route('/server')
def server():
    return render_template("server.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)
