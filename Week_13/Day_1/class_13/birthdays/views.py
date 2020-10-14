import flask
import json

from . import forms, models
from . import app, db


@app.route('/', methods=["GET", "POST"])
def index():
    form = forms.NewUserForm()
    if flask.request.method == "POST":
        name = form.name.data
        age = form.age.data

        # Create an object of a model:
        user = models.User(name=name, age=age)  # Be sure to pass keyword arguments !

        # user = {"name": name, "age": age, "msgs":[]}

        # Add this object to the database
        db.session.add(user)  # --> Receives a db.Model object

        # Commit your changes on the database:
        db.session.commit()
        print("Added user to the db !")

        # if not open(database_fn, 'r').read():
        #    users = []
        # else:
        #    users = json.load(open(database_fn, 'r'))
        # users.append(user)
        # json.dump(users, open(database_fn, 'w'))

        flask.flash(f"User {name} registered !", category="success")
    else:
        messages = models.GreetingMessage.query.all()

    return flask.render_template("index.html", form=form, messages=messages)


@app.route('/users')
def see_users():
    # Transform it to use the sqlite database (not the json one):
    users = models.User.query.all()
    # users = json.load(open(database_fn, 'r'))
    return flask.render_template('users.html', users=users)


@app.route('/birthday-of-<username>')
def birthday(username):
    # Sql query: SELECT * FROM USER

    # Fetch everything ==> users = models.User.query.all()
    # Fetch only objects where FIELD = VALUE ==> models.User.query.filter_by(FIELD=VALUE)
    user = models.User.query.filter_by(name=username).first()

    # To modify something in the database, modify it as python objects
    # and then commit the db session
    user.age += 1
    db.session.commit()

    # users = json.load(open(database_fn, 'r'))
    # for user in users:
    #    if user['name'].lower() == username.lower():
    #        user['age'] += 1
    #        break

    # json.dump(users, open(database_fn, 'w'))

    return flask.redirect(flask.url_for('see_users'))


@app.route('/users/<int:user_id>/details')
def user_details(user_id):
    user = models.User.query.get(user_id)

    return f"This user is called {user.name}"


@app.route('/greet/new', methods=("GET", "POST"))
def greet_msg():
    form = forms.NewGreetingMessageForm()

    if flask.request.method == "POST":
        msg_obj = models.GreetingMessage(content=form.content.data)
        db.session.add(msg_obj)
        db.session.commit()

        return flask.redirect(flask.url_for('index'))

    return flask.render_template('send_msg.html', form=form)