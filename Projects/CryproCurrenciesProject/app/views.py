import flask, flask_login
from . import models, forms
from . import app, db, login_mgr

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if flask.request.method == "POST":
        user_name = form.name.data
        user = models.User.query.filter_by(name=user_name).first()
        if user is None:
            flask.flash(f"There is no user with name {user_name}", 'error')
            return flask.render_template('reg.hml', form=form)

        if not user.check_password(form.pwd.data):
            flask.flash(f'Wrong password', 'error')

        flask_login.login_user(user)
        flask.flash(f'You are in {user_name}', category="success")
        return flask.redirect(flask.url_for("index"))
    return flask.render_template("login.html", form=form)

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for('index'))

@app.route('/reg', methods=["GET", "POST"])
def reg():
    form = forms.NewUser()
    if flask.request.method == "POST":
        name = form.name.data
        email = form.email.data
        pswd = form.pswd.data

        user = models.User(name=name, email=email, pswd=pswd)
        user.set_password(form.pswd.data)

        db.session.add(user)
        db.session.commit()

        flask.flash(f"{name} is registred!", category="success")

    return flask.render_template("index.html", form=form)