from app import db
from passlib.hash import pbkdf2_sha256 as sha256

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    name = db.Column(db.String)
    phone = db.Column(db.String)
    gender = db.Column(db.String)

    def __init__(self, email, password, name, phone, gender):
        self.email = email
        self.password = password
        self.name = name
        self.phone = phone
        self.gender = gender

    def __repr__(self):
        return "id: {}, name: {}, email: {}".format(self.id, self.name, self.email)

    def json(self):
        return {'id': self.id,'name': self.name, 'email': self.email}

    @classmethod
    def save_data(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def genHash(password):
        return sha256.hash(password)
    
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    @classmethod
    def getAllUsers(self):
        users = UserModel.query.all()
        res = []
        for user in users:
            obj = {'id': user.id, 'name': user.name, 'email': user.email}
            res.append(obj)
        return res

    @classmethod
    def findEmail(self, email):
        return UserModel.query.filter_by(email=email).first()
