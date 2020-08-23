import flask
import flask_login
from flask_login import UserMixin
from .mixins import ModelMixin

from . import db, login_mgr

@login_mgr.user_loader
def user_loader(user_id):
    return NewUser.query.get(user_id)

class NewUser(db.Model, UserMixin, ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(1000), unique=True)
    password = db.Column(db.String(100), unique=True)

    followers_table = db.Table('followers',
                               db.Column("follower_id", db.Integer(), db.ForeignKey("user.id")),
                               db.Column("followed_id", db.Integer(), db.ForeignKey('user.id'))
                               )

    following = db.relationship(
          "User",
          secondary=followers_table,
          primaryjoin=(followers_table.c.follower_id  == id),
          secondaryjoin=(followers_table.c.followed_id == id),
          backref="followed_by"
    )

    add_my_recipe = db.relationship("AddMyRecipe", backref="User")

    def add_my_recipe(self, post_obj):
        self.posts.append(post_obj)
        self.update()

    def set_password(self, pswd):
        self.password = pswd

    def check_password(self, pswd):
        return self.password == pswd


    def follow(self, user_id):
        if user_id == self.id:
            return True

        user = NewUser.query.get(user_id)


        if not user:
            flask.abort(404)

        self.following.append(user)

        db.session.commit()

    def __repr__(self):
        return f'<User {self.name}>'

    @classmethod
    def authenticate(cls, mail, password):
        user = cls.query.filter_by(email=mail).first()

        if user is not None and user.check_password(password):
            flask_login.login_user(user)
            return user

class RecipeSearch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingr = db.Column(db.String(50))

class AddIngr(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    add_ingr = db.Column(db.String())

class AddMyRecipe(db.Model, ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))






