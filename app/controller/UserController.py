from flask import jsonify, request
from flask_restful import reqparse
from app import app
from app.models.UserModel import UserModel

# parser = reqparse.RequestParser()
# parser.add_argument('email', type=str, required=True, help="Email field cannot be blank.")
# parser.add_argument('password', type=str, required=True, help="Password field cannot be blank.")
# parser.add_argument('name', type=str, required=True, help="Name field cannot be blank.")
# parser.add_argument('phone', type=str, required=True, help="Phone field cannot be blank.")
# parser.add_argument('gender', type=str, required=True, help="Gender field cannot be blank.")

@app.route('/user', methods=['POST'])
def save():
    try:
        body_data = request.json

        name = body_data['name']
        email = body_data['email']
        password = body_data['password']
        phone = body_data['phone']
        gender = body_data['gender']

        hashed_pass = UserModel.genHash(password);
        user = UserModel(email=email, password=hashed_pass, name=name, phone=phone, gender=gender)        
        user.save_data()

        data = {'msg': 'User created!'}
        return jsonify(data), 200
    except Exception as e:
        print(e)
        data = {'Erro': 'Something went wrong'}
        return jsonify(data), 500