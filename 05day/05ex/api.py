#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作业 用户管理（基于文件存储）

# 1. 管理员登录（写死账号是admin 密码是pwd）
# 2. 登录之后，看到用户和密码列表（存储在文件中），支持添加、删除、修改密码的操作

userlist = "user.txt"

def getuserinfo():
    ul = []
    with open(userlist) as f:
        temp = f.read().split('\n')
        for userinfo in temp:
            if userinfo != '':
                user = userinfo.split(':')[0]
                pwd = userinfo.split(':')[1]
                ul.append([user,pwd])
    return ul

def adduser(user,passwd):
    with open(userlist,"a+") as f:
        f.write("%s:%s" % (user,passwd))

user="fangtao"
with open(userlist) as f:
    name_list = f.readlines()
for name in name_list:
    temp = name.split(':')[0]
    if temp == user:
        name_list.remove(name)
print name_list
#for name in name_list:
#    with open(userlist,"w") as f:
#        f.write(name,)
    

