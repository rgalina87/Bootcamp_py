from flask_login import UserMixin
from . import db, login_mgr

@login_mgr.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(200))

    def set_password(self, pswd):
        self.pswd = pswd

    def check_password(self, pswd):
        return self.pswd == pswd

    def __repr__(self):
        return f'<User {self.name}'

class Coin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sms_id = db.Column(db.Integer, unique=True)
