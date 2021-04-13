from flask import jsonify, request
from flask_restful import reqparse
from app import app
from app.models.UserModel import UserModel, db

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True, help="Email field cannot be blank.")
parser.add_argument('password', type=str, required=True, help="Password field cannot be blank.")
parser.add_argument('name', type=str, required=True, help="Name field cannot be blank.")
parser.add_argument('phone', type=str, required=True, help="Phone field cannot be blank.")
parser.add_argument('gender', type=str, required=True, help="Gender field cannot be blank.")

@app.route('/user', methods=['POST'])
def save():
    try:
        data = parser.parse_args()

        hashed_pass = UserModel.genHash(data['password']);
        user = UserModel(email=data['email'], password=hashed_pass, name=data['name'], phone=['phone'], gender=['gender'])        
        db.session.add(user)
        db.session.commit()

        data = {'msg': 'User created.'}
        return jsonify(data), 200
    except Exception as e:
        print(e)
        data = {'Erro': 'Something went wrong'}
        return jsonify(data), 500

@app.route('/user/all', methods=['GET'])
def getUsers():
    try:
        construct = {'users': UserModel.getAllUsers()}
        return jsonify(construct)

    except Exception as e:
        data = {'Erro': str(e)}
        return jsonify(data), 500
