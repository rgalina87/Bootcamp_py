from flask_wtf import FlaskForm
import wtforms as wtf
from wtforms import validators as valid

class NewUser(FlaskForm):
    name = wtf.StringField("Name", validators=[valid.DataRequired("This field can't be empty")])
    email = wtf.StringField("Email", validators=[valid.DataRequired("This field can't be empty")])
    password = wtf.PasswordField("Password", validators=[valid.DataRequired("This field can't be empty")])
    confirm = wtf.PasswordField("Confirm password", validators=[valid.EqualTo("password")])

    submit = wtf.SubmitField("Creat a Cookbook")

class SignIn(FlaskForm):
    name = wtf.StringField("Username", validators=[valid.DataRequired("This field can't be empty")])
    password = wtf.PasswordField("Password", validators=[valid.DataRequired("This field can't be empty")])

    submit = wtf.SubmitField("Sign In")

class RecipeSearch(FlaskForm):
    ingredients = wtf.FieldList(wtf.StringField("Ingredients", render_kw={"class": "form-control"}), min_entries=1)

    submit = wtf.SubmitField("Search")

class AddRecipe(FlaskForm):
    title = wtf.StringField("Title: ")
    ingredients = wtf.TextAreaField("Ingredients: ")
    description = wtf.TextAreaField("Description: ")

    submit = wtf.SubmitField("Add Recipe!")
