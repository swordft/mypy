#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作业 用户管理（基于文件存储）
import MySQLdb as mysql

db = mysql.connect(user='root',passwd='xiaofang',db='reboot')
cur = db.cursor()

def getuserinfo():
    fields = ['name','password','email','mobile']
    sql = "select %s from users" % ','.join(fields)
    cur.execute(sql)
    res = cur.fetchall()
    users = []
    for row in res:
        user = {}
        for i,k in enumerate(fields):
	    user[k] = row[i]
	users.append(user)
    return users

def adduser(info):
    sql = "insert into users(`name`,`password`,`email`,`mobile`) values ('%s','%s','%s','%s')" % (info['name'],info['password'],info['email'],info['mobile'])
    cur.execute(sql)

def getone(id):
    sql = "select name,mobile,email from users where id=%d" %(int(id))
    cur.execute(sql)
    res = cur.fetchone()
    print res
getone(22)
def modpass(user,passwd):
    deluser(user)
    adduser(user,passwd) 

def checkuser(user,passwd):
    if len(user)==0 or len(passwd)==0:
        return False
    return True

