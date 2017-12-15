from flask import Flask
app = Flask(__name__)


# 监听一个路由 /是根目录
@app.route('/')
# 当这个路由被访问的时候，触发下面这个函数执行
def index():
    return 'hello world'

@app.route('/huoying')
def huoying():
    return 'huoying xxx'

# 启动应用
if __name__ == '__main__':
    #host允许所有ip，port监听的端口，debug调试
    app.run(host='0.0.0.0',port=9092,debug=True)
