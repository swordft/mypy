#!/usr/bin/env python
# -*- coding:utf-8 -*-

f = open('/var/log/httpd/access_log')
logs = f.read().split('\n')
f.close()

ip_dict = {}
stat_dict = {}
for line in logs:
    if line != '':
        line_list = line.split(' ')
        ip = line_list[0]
        stat = line_list[8]
        ip_dict[ip] = ip_dict.get(ip,0) + 1
        if stat != '''"-"''':
            stat_dict[stat] = stat_dict.get(stat,0) + 1

middle_ip = "<tr><td>IP</td><td>COUNT</td></tr>"
middle_stat = "<tr><td>STATUS</td><td>COUNT</td></tr>"
list_top10_ip = sorted([ (v,k) for k,v in ip_dict.items() ],reverse=True)[:10]
list_top10_stat = sorted([ (v,k) for k,v in stat_dict.items() ],reverse=True)[:10]

for i in list_top10_ip:
    ip,ip_count = i[1],i[0]
    middle_ip = middle_ip + "<tr><td>" + str(ip) + "</td><td>" + str(ip_count) + "</td></tr>"
    
for j in list_top10_stat:
    stat,stat_count = j[1],j[0]
    middle_stat = middle_stat + "<tr><td>" + str(stat) + "</td><td>" + str(stat_count) + "</td></tr>"
head = '''<table border="1"'''
end = "</table>"
res_ip = head + middle_ip + end
res_stat = head + middle_stat + end
f = open('/var/www/html/index.html','w')
f.write("IP访问次数统计:\n" + res_ip +"\n\n访问状态统计:\n" + res_stat)
f.close()


