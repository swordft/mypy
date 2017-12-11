#!/usr/bin/env python
# coding:utf-8

#def hello():
#    print 'xxx'
#    return 'hello world'

#hello
#hello()
#print hello
#print hello()

#def hello(name,action='hehe'):
#    print 'hello ' + name + action

#hello('world')

# 练习，写一个函数计算的阶乘
# 迭代：
#def jc(num):
#    res = 1
#    for i in range(1,num+1):
#        res = res*i
#    return res

#print jc(5)

# 递归
#def jc(num):
#    if num == 1:
#        return 1
#    return num*jc(num-1)

#print jc(1)

# 关键字参数
#def hello(name='woniu',job='ops'):
#    return 'my name is %s and my job is %s' %(name,job)

#print hello('reboot','python')
#print hello('python','reboot')
#print '*'*40
#print hello(job='duck')

# 收集到剩余参数
#def hello(name,*args):
#    print name,args

#hello('woniu',1,2,3,4,5,6,7)

# 写一个函数，求所有的参数之和
#def sum(*args):
#    s = 0
#    for i in args:
#        s += i
#    return s
#print sum(1,2,3,4,5,6)

#def hello(name,*args,**kargs):
#    print name,args,kargs

#hello('woniu',1,2,3,4,5,job='ops')

#def hello(ip,status):
#    print ip+':'+status

#res = [['192.1','200'],['192.2','400'],['192.2','500']]

#for r in res:
#    hello(r[0],r[1])
#    hello(*r)

# 在调用的时候，可以认为把dict展开，当成关键字参数
#res_dict = [{'ip':'192','status':'300'},{'ip':'196','status':'500'}]
#for r in res_dict:
#    hello(**r)

#def operator(name,fn):
#    fn(name)

#def sayHello(name):
#    print 'hello '+name

#def sayHehe(name):
#    print 'hehe ' +name

#operator('woniu',sayHello)
#operator('woniu',sayHehe)

# 练习：写一个排序的函数
#def my_sort(num):
#    for i in range(len(num)):
#        for j in range(i+1,len(num)):
#            if num[i] > num[j]:
#                num[i],num[j]=num[j],num[i]
#    return num
#            
#print my_sort([3,2,4,1])

# 练习：写一个排序函数，支持这两种类型的list排序
# [['192.168.0.1',10],['192.168.0.2',1],['192.168.0.3',5]]
# [{
#      'ip':'192.168.0.1',
#      'count':10
#      },{
#      'ip':'192.168.0.2',
#      'count':1
#      },{
#      'ip':'192.168.0.3',
#      'count':5
#      }]

def my_sort(num,get_key):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if get_key(num[i]) > get_key(num[j]):
                num[i],num[j]=num[j],num[i]
    return num

#def get_key_from_list(o):
#    return o[1]

#def get_key_from_dict(o):
#    return o['count']

L1 = [['192.168.0.1',10],['192.168.0.2',1],['192.168.0.3',5]]
D1 = [{
      'ip':'192.168.0.1',
      'count':10
      },{
      'ip':'192.168.0.2',
      'count':1
      },{
      'ip':'192.168.0.3',
      'count':5
      }]
#print my_sort(L1,get_key_from_list)
#print my_sort(D1,get_key_from_dict)
print my_sort(L1,lambda o:o[1])
print my_sort(D1,lambda o:o['count'])
