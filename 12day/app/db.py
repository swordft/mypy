#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Date    : 2018-05-20 08:59
# @Author  : fang tao (swordft@163.com)

import MySQLdb as mysql

#db = mysql.connect(user='root',passwd='xiaofang',db='reboot',unix_socket='/data/mysql/mysql.sock',charset='utf8')
db = mysql.connect(user='root',passwd='xiaofang',db='reboot',unix_socket='/var/lib/mysql/mysql.sock',charset='utf8')
cur = db.cursor()

# 获取表数据
def get_list(table,fields,condition=None):
    res = None
    if not condition:
        sql = "select %s from %s" % (','.join(fields),table)
        cur.execute(sql)
        result = cur.fetchall()
        if result:
            res = [dict((k,row[i]) for i,k in enumerate(fields)) for row in result]
    else:
        sql = "select %s from %s where %s" % (','.join(fields),table,condition)
        print "sql=",sql 
        cur.execute(sql)
        result = cur.fetchone()
        if result:
            res = dict((k,result[i]) for i,k in enumerate(fields))
    return res

# 插入表数据
def insert(table,fields,values):
    sql = "INSERT INTO %s(%s) VALUES (%s)" % (table,','.join(fields),','.join(["'%s'" % values[x] for x in fields]))
    cur.execute(sql)
    db.commit()

# 删除表数据
def delete(table,field,value):
    sql = "delete from %s where %s='%s'" % (table,field,value) 
    cur.execute(sql)
    db.commit()

# 更新表数据
#def update(table,field,value):
#    sql = "update %s set %s='%s' where " % (table,field,value)
#    cur.execute(sql)

#res = get_list(['name','name_cn','password','mobile','email','role','status'],'users')
#print "res=",res        
