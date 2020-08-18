import flask_login
from flask_login import UserMixin

from . import db, login_mgr

@login_mgr.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(1000), unique=True)
    password = db.Column(db.String(100), unique=True)

    def set_password(self, pswd):
        self.password = pswd

    def check_password(self, pswd):
        return self.password == pswd

    def __repr__(self):
        return f'<User {self.name}>'