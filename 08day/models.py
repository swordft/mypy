#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb as mysql

db = mysql.connect(user='root',passwd='xiaofang',db='reboot')
cur = db.cursor()

def check_user(fields,col,value):
    sql = "select %s from users where %s='%s'" % (','.join(fields),col,value)
    cur.execute(sql)
    res = cur.fetchone()
    return res

def get_userlist(fields):
    sql = "select %s from users" % ','.join(fields)
    cur.execute(sql)
    res = cur.fetchall()
    return res

def add_user(fields,values):
    sql = "insert into users (%s) values (%s)" % (fields,values)   
    cur.execute(sql)

def del_user(id):
    sql = "delete from users where id=%s" % id
    cur.execute(sql)

def update_user(id,conditions):
    sql = "update users set %s where id=%s" % (conditions,id)
    cur.execute(sql)

