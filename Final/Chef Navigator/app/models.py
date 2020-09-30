import flask
import flask_login
from flask_login import UserMixin
from .mixins import ModelMixin

from . import db, login_mgr
from . import process_data


cookbooks = db.Table('cookbooks',
                     db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
                     db.Column("recipe_id", db.Integer, db.ForeignKey("recipe.id"))
                     )

@login_mgr.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin, ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(1000))
    password = db.Column(db.String(100))
    cookbook = db.relationship("Recipe", secondary=cookbooks, backref="user")
    # posts = db.relationship("AddRecipe", backref="user")

    def add_recipe(self, recipe):
        if recipe not in self.cookbook:
            self.cookbook.append(recipe)
            db.session.commit()

    def get_cookbook_recipes(self):
        recipes=[]
        for recipe in self.cookbook:
            recipes.append(process_data.recipe_info(recipe.id))
        return recipes


    def set_password(self, pswd):
        self.password = pswd

    def check_password(self, pswd):
        return self.password == pswd


    @classmethod
    def authenticate(cls, mail, password):
        user = cls.query.filter_by(email=mail).first()

        if user is not None and user.check_password(password):
            flask_login.login_user(user)
            return user

    def __repr__(self):
        return f'<User {self.name}>'


class Recipe(db.Model, ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))

    @classmethod
    def get_or_create(cls, id, name):
        obj = cls.query.get(id)
        if not obj:
            obj = cls(id=id, name=name)
            obj.save()
        return obj


        # --Future upgrades--
class AddRecipe(db.Model, ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    # def add_my_post(self, post):
    #     self.posts.append(post)
    #     self.update()

    # followers_table = db.Table('followers',
    #                            db.Column("follower_id", db.Integer(), db.ForeignKey("user.id")),
    #                            db.Column("followed_id", db.Integer(), db.ForeignKey('user.id'))
    #                            )

    # following = db.relationship(
    #       "User",
    #       secondary=followers_table,
    #       primaryjoin=(followers_table.c.follower_id == id),
    #       secondaryjoin=(followers_table.c.followed_id == id),
    #       backref="followed_by"
    # )


    # def follow(self, user_id):
    #     if user_id == self.id:
    #         return True
    #
    #     user = User.query.get(user_id)
    #
    #
    #     if not user:
    #         flask.abort(404)
    #
    #     self.following.append(user)
    #
    #     db.session.commit()
