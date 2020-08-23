from datetime import datetime

from . import db

class ModelMixin:

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    modified_on = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except:
            db.session.rollback()

        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()