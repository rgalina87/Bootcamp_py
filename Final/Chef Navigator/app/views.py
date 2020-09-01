import flask
import flask_login

from . import app, db, login_mgr
from . import forms, models, process_data



@app.route('/')
def start_page():
    return flask.render_template("start_page.html")

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    user = flask_login.current_user
    if not user:
        flask.abort(404)

    return flask.render_template("profile.html", user=user)

# @app.route("/profile/<int:user_id>/follow")
# def follow_user(user_id):
#     if flask_login.current_user.is_anonymous:
#         return flask.redirect(flask.url_for('sign_in'))
#
#     flask_login.current_user.follow(user_id)

    # return flask.redirect(flask.url_for('profile', user_id=user_id))

# @app.route('/add_my_post', methods=['GET', 'POST'])
# @flask_login.login_required
# def add_my_post():
#
#     add_my_post = forms.AddRecipe()
#
#     return flask.render_template("add_my_recipe.html", form=add_my_post)

# @app.route('/add_my_recipe', methods=['GET', 'POST'])
# def add_my_recipe():
#     form = forms.AddRecipe()
#     if form.validate_on_submit():
#        post = models.AddRecipe(
#            title=form.title.data,
#            ingredients=form.title.data,
#            description=form.title.data
#            )
#
#        db.session.add(post)
#        db.session.commit()
#        return flask.redirect(flask.url_for ('my_recipe'))
#     else:
#         flask.flash("Something goes wrong", "danger")
#         return flask.render_template("add_my_recipe.html", form=form)


# @app.route("/post/<int:post_id>", methods=['GET', 'POST'])
# @flask_login.login_required
# def view_post(post_id):
#
#     post = models.AddRecipe.query.get(post_id)
#
#     return flask.render_template("my_recipe.html", post=post)


@app.route('/recipe_search', methods=['GET', 'POST'])
def recipe_search():
    form = forms.RecipeSearch()
    if form.validate_on_submit():

        print(form.ingredients)

        recipes = process_data.search_by_ingredient(ingredients=form.ingredients.data)
        # print(recipes)
        return flask.render_template("results.html", recipes=recipes)

    return flask.render_template("recipe_search.html", form=form)

@app.route('/add_recipe/<int:recipe_id>-<recipe_name>', methods=['GET', "POST"])
def add_recipe(recipe_name, recipe_id):
    recipe = models.Recipe.get_or_create(
        recipe_id,
        recipe_name
    )
    flask_login.current_user.add_recipe(recipe)
    return "ok"

@app.route('/saved_recipes', methods=['GET', 'POST'])
def saved_recipes():

    print(flask_login.current_user.cookbook)

    return flask.render_template("saved_recipes.html")

@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():

    form = forms.SignIn()
    if form.validate_on_submit():
        user = models.User.authenticate(
            form.email.data,
            form.password.data
        )

        if user is not None:
            flask.flash("Login successful", 'success')
            return flask.redirect(flask.url_for('profile'))

        flask.flash("Wrong user mail or password", 'danger')
    else:
        print(form.errors)
    return flask.render_template('sign_in.html', form=form)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for("start_page"))


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    form = forms.User()
    if form.validate_on_submit():
        user = models.User(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data,
                   )

        db.session.add(user)
        db.session.commit()
        return flask.redirect(flask.url_for('profile'))
    else:
        if form.errors:
            print(form.errors)

    return flask.render_template("sign_up.html", form=form)


