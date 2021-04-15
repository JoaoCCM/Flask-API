from flask import jsonify, request
from flask_restful import reqparse
from app import app
from flask_jwt_extended import create_access_token, create_refresh_token
from app.models.UserModel import UserModel

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True, help="Email field cannot be blank.")
parser.add_argument('password', type=str, required=True, help="Password field cannot be blank.")

@app.route('/signIn', methods=['POST'])
def signIn():
    try:
        data = parser.parse_args()

        user = UserModel.findEmail(data['email'])
        if not user:
            raise Exception('User not found')

        if UserModel.verify_hash(data['password'], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)

            res = {"access_token": access_token, "refresh_token": refresh_token}

            return jsonify(res)

        else:
            data = {'message': 'Wrong credentials'}
            return jsonify(data), 500


    except Exception as e:
        data = {'Erro': str(e)}
        return jsonify(data), 500
