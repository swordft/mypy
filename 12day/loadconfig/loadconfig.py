#!/usr/bin/env python

import os
from flask import Flask
from config import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    if os.path.exists('/tmp/online'):
    #app.config.from_object(ProductionConfig)
        app.config.from_object(config['pro'])
        print app.config.get('SQLALCHEMY_DATABASE_URI')
    else:
        app.config.from_object(config['dev'])
        print app.config.get('SQLALCHEMY_DATABASE_URI')
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9999,debug=True)
