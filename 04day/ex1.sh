#!/usr/bin/env python
# -*- coding=utf-8 -*-
#作业1：上节课作业统计结果用函数优化

def analog(log):
    f = open(log)
    res_dict = {}
    for line in f:
        if line == '\n':
            continue
        temp = line.split()
        ip,status = temp[0],temp[8]
        tup = (ip,status)
        res_dict[tup] = res_dict.get(tup,0) + 1
    f.close()
    res_list = res_dict.items()
    for j in range(len(res_list)-1):
        for i in range(len(res_list)-1):
            if res_list[i][1] < res_list[i+1][1]:
                res_list[i],res_list[i+1] = res_list[i+1],res_list[i]
    return res_list

def makeweb(data,webdir):
    html_str = '<table border="1">'
    html_str += '<tr><td>IP</td><td>STATUS</td><td>count</td></tr>'
    tr_temp = '<tr><td>%s</td><td>%s</td><td>%s</td></tr>'
    for (ip,status),count in data:
        html_str += tr_temp %(ip,status,count)
    html_f = open(webdir,'w')
    html_f.write(html_str)
    html_f.close()

logfile = '/var/log/httpd/access_log'
index_dir = '/var/www/html/index.html'
res_statistic = analog(logfile)
makeweb(res_statistic,index_dir)

