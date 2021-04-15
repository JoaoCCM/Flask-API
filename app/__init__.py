from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
import os

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://{}:{}@localhost:5432/flask'.format(os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['JWT_SECRET_KEY']=os.getenv('JWT_SECRET')

jwt = JWTManager(app)

@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({'Description':'Token Expired'}), 401

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controller.UserController import *
from app.controller.AuthController import *

