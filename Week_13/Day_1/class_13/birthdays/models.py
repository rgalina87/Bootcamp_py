from . import db

# First - Create a class_13 that inherit from db.Model
class User(db.Model):

    # Second - Create your model's columns
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    age  = db.Column(db.Integer)

    def __repr__(self):
        return f"<User {self.name}>"

class GreetingMessage(db.Model):

    id      = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)