from flask_wtf import FlaskForm
import wtforms as wtf
from wtforms import validators as valid

class PhoneUser(FlaskForm):

    submit = wtf.SubmitField("")
    pass
