# from ex import db
#
# class Phone(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
#     email = db.Column(db.String(), unique=True)
#     phone_number = db.Column(db.String(10), unique=True)
#     address = db.Column(db.String())
#
#     def __repr__(self):
#         return f"<Phone {self.phone_number}>"