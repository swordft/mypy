#!/usr/bin/env python
# -*- coding:utf-8 -*-

#import hello

#hello.hi()
#hello.hi('fangtao')

#from hello import hi,num
#hi('ooo')
#print num

#import hello as h
#h.hi()

# request获取参数 request.args.get(key)
# render_template 渲染模板文件，默认的模板文件在templates文件夹下面
#from flask import Flask,request,render_template
#app = Flask(__name__)

#@app.route('/')
#def index():
#    return render_template('index.html')

#@app.route('/huoying')
#def huoying():
#    user = request.args.get('username')
#    pwd = request.args.get('password')
#    return 'huoying %s:%s' %(user,pwd)

#if __name__ == '__main__':
#    app.run(host='0.0.0.0',port=9092,debug=True)


# 据说get由长度限制，其实没有，因为长度限制是浏览器做的，与http协议无关
# 据说get不安全，post安全，其实没有，因为http都是明文传输，get的数据在url里，post的数据在表单里
# get是幂等的，调用多少次结果都是一样的，post不是幂等

#from flask import Flask,request,render_template,redirect
#app = Flask(__name__)
#
#@app.route('/')
#def index():
#    return render_template('login.html')
#
#def check_login(user,pwd):
#    with open('user.txt') as f:
#        user_list = f.read().split('\n')
#        user_pwd = '%s:%s' % (user,pwd)
#        if user_pwd in user_list:
#            return 'success'
#        else:
#            return 'error'
#    
#@app.route('/login')
#def huoying():
#    user = request.args.get('user')
#    pwd = request.args.get('pwd')
#    return check_login(user,pwd)
#
#if __name__ == '__main__':
#    app.run(host='0.0.0.0',port=9092,debug=True)


from flask import Flask,request,render_template,redirect
app = Flask(__name__)

@app.route('/')
def index():
    user_list = [['user','pwd'],['fangtao','xiaofang'],['wjx','wjx']]
    return render_template('login.html',error_msg='xxx',ulist=user_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)
