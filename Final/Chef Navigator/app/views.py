import flask
import flask_login

from . import app, db, login_mgr
from . import forms, models, process_data

@app.route('/')
def start_page():
    return flask.render_template("start_page.html")

# @app.route('/profile/<int:user_id>')
# def profile(user_id):
#     user = models.NewUser.query.get(user_id)
#     if not user:
#         flask.abort(404)
#     return flask.render_template("profile.html", user=user)

@app.route('/profile')
def profile():
    return flask.render_template("profile.html")

# @app.route('/add_my_recipe', methods=['GET', 'POST'])
# def add_my_recipe():
#
#     add_my_post = forms.AddRecipe()
#
#     return flask.render_template("add_my_recipe.html", form=add_my_post)

# @app.route("/post/<int:post_id>")
# def view_post(post_id):
#     post = models.AddRecipe.query.get(post_id)
#
#     return flask.render_template("my_recipe.html", post=post)


@app.route('/recipe_search', methods=['GET', 'POST'])
def recipe_search():
    form = forms.RecipeSearch()
    if form.validate_on_submit():

        print(form.ingredients)

        recipes = process_data.search_by_ingredient(ingredients=form.ingredients.data)

        return flask.render_template("results.html", recipes=recipes)

    return flask.render_template("recipe_search.html", form=form)

# @app.route('/recipe/<int:recipe_id>', methods=['GET', 'POST'])
# def recipe(recipe_id):
#     return flask.render_template("recipe.html", recipe_id=recipe_id)


# @app.route('/results/', methods=['GET', 'POST'])
# def result():
#     return flask.render_template("results.html")


 #проверить линк html
@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():

    form = forms.SignIn()
    if form.validate_on_submit():
        user = models.NewUser.authenticate(
            form.email.data,
            form.password.data
        )
        if user is not None:
            flask.flash("Login successful", 'success')
            return flask.redirect(flask.url_for('portfolio'))

        flask.flash("Wrong user mail or password", 'danger')

    return flask.render_template('sign_in.html', form=form)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for("start_page.html"))


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    form = forms.SignIn()
    if form.validate_on_submit():
        user = models.NewUser(
            Name=form.name.data,
            Email=form.email.data,
            Password=form.password.data
                   )

        db.session.add(user)
        db.session.commit()
        return flask.redirect(flask.url_for('portfolio'))
    else:
        print(form.errors)

    return flask.render_template("sign_up.html", form=form)


