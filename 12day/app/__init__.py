from flask import Flask

app = Flask(__name__)
app.secret_key="1q2w3e4R"

from admin import *
from cmdb import *
