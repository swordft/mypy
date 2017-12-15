#!/usr/bin/env python
# -*- coding:utf-8 -*-

def formatNum(num):
    o = 'KB'
    if num>1024*1024:
        num/=(1024*1024)
        o='GB'
    elif num>1024:
        num/=1024.0
        o='MB'
    return '%.2f%s' %(num,o)

def get_mem_info(arr):
    tmp = arr.split()
    tmp[1] = formatNum(float(tmp[1]))
    return tmp[:2]

def operate(key):
    with open('/proc/meminfo') as f:
        mem_total = key(f.readline())
        mem_free = key(f.readline())
        mem_available = key(f.readline())
        mem_buf = key(f.readline())
        mem_cache = key(f.readline())
        return mem_total,mem_free,mem_available,mem_buf,mem_cache

def get_html(arr):
    html_str = '<table border=1>'
    for mem in arr:
        html_str +='<tr><td>%s</td><td>%s</td></tr>' %tuple(mem)
    return html_str

def gen_html(html_s):
    with open('/var/www/html/mem.html','w') as f:
        f.write(html_s)

def getMem():
    mem_info = operate(get_mem_info)
    return get_html(mem_info)

if __name__ == '__main__':
    html_s = getMem()
    gen_html(html_s)
