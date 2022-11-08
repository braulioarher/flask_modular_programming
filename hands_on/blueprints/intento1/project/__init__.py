from flask import Flask

from .extensions import db, migrate
from .views.StudentView import student
from .views.TeacherView import teacher
import os

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():

    #app intialization
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'hello.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


    #db inititalization
    db.init_app(app)
    migrate.init_app(app, db)

    #Register the views in student view and teacher view as blueprints using the following prefixes.
    # url_prefix for teachers: /api/teachers
    app.register_blueprint(teacher)
    # url_prefix for students: /api/students
    app.register_blueprint(student)
    return app
