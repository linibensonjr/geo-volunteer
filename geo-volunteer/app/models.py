import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
# app.config['SECRET_KEY'] = 'mysecret'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

