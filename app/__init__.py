from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://{}:{}@localhost:5432/flask'.format(os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controller.UserController import *

