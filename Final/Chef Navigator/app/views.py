import flask
import flask_login


from . import app, db
from . import forms, models, process_data

@app.route('/')
def start_page():
    return flask.render_template("start_page.html")

@app.route('/profile')
def profile():
    # user = models.User.query.get()
    # if not user:
    #     flask.abort(404)

    return flask.render_template("profile.html")

@app.route('/my_recipe')
def my_recipe():

    return flask.render_template("my_recipe.html")

@app.route('/add_my_recipe')
def add_my_recipe():
    return flask.render_template("add_my_recipe.html")


@app.route('/recipe_search', methods=['GET', 'POST'])
def recipe_search():
    form = forms.RecipeSearch()
    if flask.request.method == "POST":

        get_recipe = process_data.search_by_ingrediant(forms.RecipeSearch())

    return flask.render_template("recipe_search.html", form=form, get_recipe=get_recipe)

# @app.route('/add_ingr/', methods=['GET', 'POST'])
# def add_ingr():
#         return flask.render_template("recipe_search.html")

 #проверить линк html
@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = forms.SignIn()
    if form.validate_on_submit():
        user_name = form.name.data
        user = models.User.query.filter_by(name=user_name).first()
        if user is None:
            flask.flash(f"User {user_name} doesn't exist", 'error')
            return flask.render_template('sign_in.html', form=form)

        if not user.check_password(form.pswd.data):
            flask.flash(f"Wrong password", 'error')
            return flask.render_template('sign_in.html', form=form)

        flask_login.login_user(user)
        flask.flash(f"Hi {user_name}", category="sucess")

        return flask.redirect(flask.url_for('index'))


    return flask.render_template("sign_in.html", form=form)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for("start_page.html"))


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = forms.NewUser()
    if form.validate_on_submit():
        user = models.User(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data
        )

        db.session.add(user)
        db.session.commit()

        flask.flash(f'Welcome')

        return flask.redirect(flask.url_for("portfolio.html"))
    else:
        "Error"

    return flask.render_template("sign_up.html", form=form)


