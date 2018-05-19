from flask import render_template
from . import app

@app.route('/views')
def views():
    return "hello views"
