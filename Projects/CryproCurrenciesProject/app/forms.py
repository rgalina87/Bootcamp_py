from flask_wtf import FlaskForm
import wtforms as wtf
from wtforms import validators as valid

from . import models

class LoginForm(FlaskForm):
    name = wtf.StringField("Name", validators=[valid.DataRequired("This field can't be empty")])
    pwd  = wtf.PasswordField("Password", validators=[valid.DataRequired("This field can't be empty")])

    submit = wtf.SubmitField("Log In")

class NewUser(FlaskForm):
    name = wtf.StringField("Name")
    email = wtf.StringField("Email", validators=[valid.Email])
    pswd = wtf.PasswordField("Password")

    submit = wtf.SubmitField("Create account")

