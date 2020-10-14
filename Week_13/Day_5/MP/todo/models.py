import datetime
from . import db

class Todolist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    to_do = db.Column(db.String(500))
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    complete = db.Column(db.Boolean)


    def __repr__(self):
        return f"<Todolist {self.to_do}>"