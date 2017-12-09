#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 把ip和状态码作为一个元组
f = open('/var/log/httpd/access_log')

res_dict = {}
for line in f:
    if line == '\n':
        continue
    temp = line.split()
    ip = temp[0]
    status = temp[8]
    tup = (temp[0],temp[8])
    res_dict[tup] = res_dict.get(tup,0) + 1
f.close()

res_list = res_dict.items()
for j in range(len(res_list)-1):
    for i in range(len(res_list)-1):
        if res_list[i][1] < res_list[i+1][1]:
            res_list[i],res_list[i+1] = res_list[i+1],res_list[i]

# 生成html文件
html_str = '<table border="1">'
html_str += '<tr><td>IP</td><td>STATUS</td><td>count</td></tr>'
tr_temp = '<tr><td>%s</td><td>%s</td><td>%s</td></tr>'

for (ip,status),count in res_list:
    html_str += tr_temp %(ip,status,count)

# 将html文件写入到httpd的主页文件中
html_f = open('/var/www/html/index.html','w')
html_f.write(html_str)
html_f.close()

