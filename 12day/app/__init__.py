from flask import Flask

app = Flask(__name__)

from admin import *
from views import *
