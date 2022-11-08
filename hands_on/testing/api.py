#Use this app for testing
from flask import Flask, request, jsonify,  make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#app intialization
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usermanagement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


#db inititalization
db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)

from src.views.UserView import user_api as user_blueprint


app.register_blueprint(user_blueprint, url_prefix="/users")