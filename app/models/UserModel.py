from app import db
from passlib.hash import pbkdf2_sha256 as sha256

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    name = db.Column(db.String(80))
    phone = db.Column(db.String(20))
    gender = db.Column(db.String(10))

    def __init__(self, email, password, name, phone, gender):
        self.email = email
        self.password = password
        self.name = name
        self.phone = phone
        self.gender = gender

    def __repr__(self):
        return "<Name: {},".format(self.name)

    @classmethod
    def save_data(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def genHash(password):
        return sha256.hash(password)