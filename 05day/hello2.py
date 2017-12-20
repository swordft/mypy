from flask import Flask
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
app = Flask(__name__)

class NameForm(Form):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')

#form = NameForm()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)
