#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 使用pickle实现增删改查
import pickle

# 增加
def Create(username,password):
    users = {username:password}
    with open('user.txt','wb') as f:
        pickle.dump(users,f)

# 删除
def Delete(user):
    content = {}
    with open('user.txt') as f:
        content = pickle.load(f)
    content.pop(user)
    with open('user.txt','wb') as f:
        pickle.dump(content,f)

# 修改
def Modify(user,password):
    content = {}
    with open('user.txt') as f:
        content = pickle.load(f)
    content[user] = password
    with open('user.txt','wb') as f:
        pickle.dump(content,f)

# 查看所有
def Select():
    content = {}
    with open('user.txt') as f:
        content = pickle.load(f)
    print content
    for k,v in content.items():
        print "用户信息：%s ---> %s" % (k,v)

# 查看某条数据
def SelectOne(username):
    user = username
    userinfo = {}
    with open('user.txt') as f:
        content = pickle.load(f)
    userinfo[user] = content[user]
    return userinfo

Create('fangtao','xiaofang')
Modify('wjx','wjx')
Modify('wangjuan','wangjuan')
Select()
