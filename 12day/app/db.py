#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Date    : 2018-05-20 08:59
# @Author  : fang tao (swordft@163.com)

import MySQLdb as mysql

db = mysql.connect(user='root',passwd='xiaofang',db='reboot',unix_socket='/data/mysql/mysql.sock',charset='utf8')
cur = db.cursor()

# 获取表数据
def get_list(fields,table,name=None):
    res = None
    if not name:
        sql = "select %s from %s" % (','.join(fields),table)
        cur.execute(sql)
        result = cur.fetchall()
        if result:
            res = [dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
    else:
        sql = "select %s from %s where name='%s'" % (','.join(fields),table,name)
        cur.execute(sql)
        result = cur.fetchone()
        if result:
            res = dict((k,result[i]) for i,k in enumerate(fields))
    return res

#res = get_list(['name','name_cn','password','mobile','email','role','status'],'users')
#print "res=",res        
