import flask
import flask_login


from . import app, db
from . import forms, models

@app.route('/')
def start_page():
    return flask.render_template("start_page.html")

@app.route('/profile')
def profile():
    # user = models.User.query.get()
    # if not user:
    #     flask.abort(404)

    return flask.render_template("profile.html")



@app.route('/recipe_search')
def recipe_search():
    return flask.render_template("recipe_search.html")

#??????????????
# @app.route('/add_ingr/', methods=['GET', 'POST'])
# def add_ingr():
#     form = forms.Add_ingr()
#     if flask.request.method == 'POST':
#         new_ingr = form.new_ingr
#     return flask.render_template("recipe_search.html", form=form, new_ingr=new_ingr)

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


    return flask.render_template('sign_in.html', form=form)

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

        return flask.redirect(flask.url_for("start_page.html"))
    else:
        "Error"

    return flask.render_template("sign_up.html", form=form)