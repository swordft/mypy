#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 作业 用户管理（基于文件存储）

# 1. 管理员登录（写死账号是admin 密码是pwd）
# 2. 登录之后，看到用户和密码列表（存储在文件中），支持添加、删除、修改密码的操作

userlist = "user.txt"

def getuserinfo():
    ul = {}
    with open(userlist) as f:
        temp = f.read().split('\n')
        for userinfo in temp:
            if userinfo != '':
                temp = userinfo.split(':')
                ul[temp[0]] = temp[1]
    return ul

def adduser(user,passwd):
    with open(userlist,"a") as f:
        f.write("%s:%s\n" % (user,passwd))

def deluser(user):
    with open(userlist) as f:
        name_list = f.readlines()
    for name in name_list:
        temp = name.split(':')[0]
        if temp == user:
            name_list.remove(name)
    with open(userlist,"w") as f_temp:
        f_temp.write("")
    with open(userlist,"a") as f:
        for name in name_list:
            f.write(name)

def modpass(user,passwd):
    deluser(user)
    adduser(user,passwd) 

def checkuser(user,passwd):
    if len(user)==0 or len(passwd)==0:
        return False
    return True

