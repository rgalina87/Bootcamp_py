
#!/usr/local/bin/python3

from flask_wtf import FlaskForm
import wtforms as wtf
from wtforms import validators as valid

class NewUserForm(FlaskForm):
    name = wtf.StringField("Name")
    age  = wtf.IntegerField("Age")

    submit = wtf.SubmitField("Create user")

class NewGreetingMessageForm(FlaskForm):

    content = wtf.StringField("Content")

    submit = wtf.SubmitField("Post")
