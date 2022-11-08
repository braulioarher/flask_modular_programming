from flask import Flask, request, jsonify,  make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#app intialization
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schoolmanagement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


#db inititalization
db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)


#Register the views in student view and teacher view as blueprints using the following prefixes.
from src.views import StudentView, TeacherView
# url_prefix for teachers: /api/teachers
app.register_blueprint(TeacherView.teacher, url_prefix="/api/teachers")
# url_prefix for students: /api/students
app.register_blueprint(StudentView.student, url_prefix="/api/students")

