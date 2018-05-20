#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Date    : 2018-05-20 08:59
# @Author  : fang tao (swordft@163.com)

import MySQLdb as mysql

db = mysql.connect(user='root',passwd='xiaofang',db='reboot',unix_socket='/var/lib/mysql/mysql.sock',charset='utf8')
cur = db.cursor()

# 获取用户信息列表
def get_list(fields,table,id=None):
    if not id:
        sql = "select %s from %s" % (','.join(fields),table)
        cur.execute(sql)
    else:
        sql = "select %s from %s where id='%s'" % (','.join(fields),table,id)
        cur.execute(sql)
    result = cur.fetchall()
    res = [dict((k,row[i]) for i,k in enumrate(fields)) for row in result]
    return res
        
