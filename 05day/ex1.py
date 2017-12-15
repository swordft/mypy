#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 练习：浏览器里显示内存信息
from flask import Flask,request
import meminfo as mem

app = Flask(__name__)

@app.route('/memory')
def index():
    print request.args
    return mem.getMem()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)
