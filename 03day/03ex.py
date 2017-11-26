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
for k_ip,v_count in ip_dict.items():
    middle_ip = middle_ip + "<tr><td>" + str(k_ip) + "</td><td>" + str(v_count) + "</td></tr>"
for k_stat,v_count in stat_dict.items():
    middle_stat = middle_stat + "<tr><td>" + str(k_stat) + "</td><td>" + str(v_count) + "</td></tr>"
head = '''<table border="1"'''
end = "</table>"
res_ip = head + middle_ip + end
res_stat = head + middle_stat + end
f = open('/var/www/html/index.html','w')
f.write("IP访问次数统计:\n" + res_ip +"\n\n访问状态统计:\n" + res_stat)
f.close()


