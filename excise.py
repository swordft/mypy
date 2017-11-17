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
input_num = int(raw_input("Please input number: "))
arr = [1,3,7,10,22,100,299,1000,2000,30000,40000]
start = 0
end = len(arr) - 1
while True:
    mid = (start+end)/2
    mid_num = arr[mid]
    if input_num < mid_num:
        end = mid
    elif input_num > mid_num:
        start = mid
    else:
        print 'find',mid
        break
