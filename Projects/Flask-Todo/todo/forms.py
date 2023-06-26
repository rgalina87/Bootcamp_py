from flask_wtf import FlaskForm
import wtforms as wtf
from wtforms import validators as valid

class Todo():
    task_content = wtf.StringField("content")

    submit = wtf.SubmitField("Add Task")

