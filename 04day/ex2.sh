#!/usr/bin/env python
# -*- coding=utf-8 -*-
#作业2：实战函数tail -f 的功能

import time

def tail(logfile): 
    f = open(logfile)
    while True:
        content = f.read()
        if content:
            print content
        time.sleep(1)

log = '/var/log/httpd/access_log'
tail(log)
