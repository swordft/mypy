#!/usr/bin/env python
# -*- coding=utf-8 -*-
#作业3：获取占用内存的函数 getMem()，每秒打印一个
import time,os

def getMem():
    meminfo = os.popen('cat /proc/meminfo').readlines()[2].split(' ')[5]
    return meminfo

while True:
    memory = getMem()
    print "系统可用内存为: %s Kb" % memory
    time.sleep(1)


