import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# ------------- SQLAlchemy configuration ---------------------------
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'ksdnvipeusrgnwe32423n32oin32knihfico3n'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'CHAT.sqlite3')
# ------------------------------------------------------------------

db = SQLAlchemy(app)    # Database ORM
ma = Marshmallow(app)   # Data Models Serializer
bcrypt = Bcrypt(app)    # Password-Hashing Function
jwt = JWTManager(app)   # JSON Web Token Encoder/Decoder

from chatapi import routes

#db.create_all()


