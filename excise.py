#!/usr/bin/env python
# -*- coding:utf8 -*-

#name = raw_input('please input your name: ')
#if name == 'reboot':
#    print 'hello reboot'
#    print 'haha'
#

#name = ''
#while not name:
#    name = raw_input('input your name: ')
#
#print 'hello ' + name

#money = 10000
#year = 0
#
#while money < 20000:
#    money = money*(1+0.0325)
#    year = year + 1
#
#print money
#print year


#for name in ['fangtao','wjx','swk']:
#    print name

#lst1 = ['C','js','python','js','css','js','html','node']
#stat = {}
#for lan in lst1:
#    if lan not in stat.keys():
#        stat[lan] = 1
#    stat[lan] += 1
#print stat

#lst1 = ['C','js','python','js','css','js','html','node']
#count = 0
#for lan in lst1:
#    if lan == 'js':
#        count += 1
#print "The word 'js' is appeared %s times." % count

#lst1 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

#max = 0
#for num in lst1:
#    if num > max:
#        max = num
#print 'max number is ' + str(max)

#i = 0
#while i < 10:
#    i += 1
#    if i == 7:
#        break
#    print i

#while True:
#    year = int(raw_input("Input year: "))
#    if year % 100 == 0 and year % 400 == 0:
#        print "%s is run year!" % year
#        break
#    elif year % 100 !=0 and year % 4 == 0:
#        print "%s is run year!" % year
#        break
#    print "%s is not run year,please input again." % year

#lst1 = [1,2,3,65555,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
#max1 = lst1[0]
#max2 = 0
#for num in lst1:
#    if num > max1:
#        temp = max1
#        max1 = num
#        max2 = temp
#    elif num <= max1 and num > max2:
#        max2 = num
#
#print "Two max numbers are %s and %s" % (max1,max2)

#冒泡排序
#lst1 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
#count = len(lst1)
#for x in range(count):
#    for y in range(x+1,count):
#        if lst1[x] > lst1[y]:
#            lst1[x],lst1[y] = lst1[y],lst1[x]    
#print "The max number is %s,the second max number is %s" % (lst1[count-1],lst1[count-2])

#九九乘法表
#for x in range(1,10):
#    for y in range(1,x+1):
#        print "%d*%d=%d" % (x,y,x*y),
#    print

#让用户输入一个数组，如何最快的找到用户输入数字的索引
#arr是从小到大排好序的list
#input_num = int(raw_input("Please input number: "))
#arr = [1,3,7,10,22,100,299,1000,2000,30000,40000]
#start = 0
#end = len(arr) - 1
#while True:
#    mid = (start+end)/2
#    mid_num = arr[mid]
#    if mid == start:
#        print "cannot find!"
#        break
#    if input_num < mid_num:
#        end = mid
#    elif input_num > mid_num:
#        start = mid
#    else:
#        print 'find',mid
#        break

#冒泡排序2
#arr = [3,7,18,2,20,99,1,54]
#count = len(arr)-1
#loop_cnt = 0
#for x in range(count):
#    for y in range(x+1,count):
#        if arr[x]>arr[y]:
#            arr[x],arr[y] = arr[y],arr[x]
#        loop_cnt += 1
#    loop_cnt += 1
#
#print "max number is %s" % arr[-1]
#print "execute %s times" % loop_cnt

#数组去重
#arr = [1,2,3,4,4,12,3,14,3,2,21,12,4111,3333,22,21]
#arr_uniq = []
#for i in arr:
#    if i not in arr_uniq:
#        arr_uniq.append(i)
#print arr_uniq

#求两个数组共同的值
#arr1 = [1,2,3,4,2,12,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
#arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]

#arr_new = []
#for i in arr2:
#    if i in arr1 and i not in arr_new:
#        arr_new.append(i)
#print arr_new

#用户名密码用:分隔，让用户输入用户名和密码，判断能否登录
#方法一:
#arr = ['user:pwd','user1:pwd1','user2:123']
#user = raw_input("input username: ")
#password = raw_input("input password: ")
#auth_info = ':'.join([user,password])
#if auth_info in arr:
#    print "login success!"
#else:
#    print "login error!"

#方法二:
#arr = ['user:pwd','user1:pwd1','user2:123']
#user = raw_input('input username: ')
#password = raw_input('input password: ')

#user_exists = False
#for u in arr:
#    if user != u:
#        break
#    temp = u.split(':')
#    if temp[1] == password:
#        msg = 'success'
#    else:
#        msg = 'wrong password!'
#    print msg
#    user_exists = True
#    break
#if not user_exists:
#    print 'user not exists'

#用户密码对照表在user.txt文件中，手机号和用户密码都可以登录
#f = open('user.txt')
#info = f.read().split('\n')
#f.close()
#input_user = raw_input('input username: ')
#input_pwd = raw_input('input password: ')
#for u in info:
#    temp = u.split(':')
#    if input_user == temp[1] or input_user == temp[0]:
#        if input_pwd == temp[2]:
#            print 'success!'
#            break
#        else:
#            print 'password error!'
#            break
#    else:
#        print 'user not exists!'
#        break

#统计文本文件中所有字符出现的次数
#f = open('context.txt')
#context = f.read()
#f.close()

#res = {}
#for word in context.split(' '):
#    res[word] = res.get(word,0) + 1
#print res

#把上一题的结果，打印前10名
#f = open('context.txt')
#context = f.read()
#f.close()
#
#res = {}
#for word in context.split(' '):
#    res[word] = res.get(word,0) + 1
#
#res_list = []
#for k in res:
#    res_list.append([k,res[k]])
#
#for x in range(10):
#    for y in range(x+1,len(res_list)):
#        if res_list[x][1]<res_list[y][1]:
#            res_list[x],res_list[y] = res_list[y],res_list[x]
#                
#for r in res_list[:10]:
#    print "word '%s' count is %s" %(r[0],r[1])
#    
#    


#反转dict，变成 value:key ,然后把值取出，sort排序把前10取出来，然后遍历，去反转后的dict里获取字符
f = open('context.txt')
context = f.read()
f.close()

res = {}
for word in context.split(' '):
    res[word] = res.get(word,0) + 1

res_rev = {}
res_list = []
for k in res:
    if res[k] in res_rev:
        res_rev[res[k]].append(k)
    else:
        res_rev[res[k]] = [k]

key_list = []
for k in res_rev:
    key_list.append(k)
key_list.sort()

for count in range(10):
    if count>len(res_rev)-1:
        break
    value = res_rev[key_list[count]]
    print "char '%s' count is %s" %(','.join(value),key_list[count])
