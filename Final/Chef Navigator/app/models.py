import flask
import flask_login
from flask_login import UserMixin
from .mixins import ModelMixin

from . import db, login_mgr

followers_table = db.Table('followers',
                           db.Column("follower_id", db.Integer(), db.ForeignKey("user.id")),
                           db.Column("followed_id", db.Integer(), db.ForeignKey('user.id'))
                           )

@login_mgr.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin, ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(1000))
    password = db.Column(db.String(100))



    following = db.relationship(
          "User",
          secondary=followers_table,
          primaryjoin=(followers_table.c.follower_id == id),
          secondaryjoin=(followers_table.c.followed_id == id),
          backref="followed_by"
    )

    add_my_post = db.relationship("AddRecipe", backref="user")


    def add_my_post(self, post_obj):
        self.posts.append(post_obj)
        self.update()

    def set_password(self, pswd):
        self.password = pswd

    def check_password(self, pswd):
        return self.password == pswd


    def follow(self, user_id):
        if user_id == self.id:
            return True

        user = User.query.get(user_id)


        if not user:
            flask.abort(404)

        self.following.append(user)

        db.session.commit()

    @classmethod
    def authenticate(cls, mail, password):
        user = cls.query.filter_by(email=mail).first()

        if user is not None and user.check_password(password):
            flask_login.login_user(user)
            return user

    def __repr__(self):
        return f'<User {self.name}>'


class AddRecipe(db.Model, ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    # user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

# class SearchResult(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     image = db.Column(db.String())
#     title = db.Column(db.String(10000))
#     ingredients = db.Column(db.Text)
#     description = db.Column(db.Text)






