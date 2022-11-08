import re
from flask import request, json, Response, Blueprint
from flask import render_template
from flask_cors import CORS, cross_origin
from ..extensions import db
from ..models.StudentModel import StudentModel, StudentSchema


#Add your code here
student = Blueprint('student', __name__)
# Create routes to add a student to the database.
@student.route('/students/add/', methods=['POST'])
def create_student():
    if request.method == 'POST':
        info = request.data
        data = json.loads(info)
        add1 = StudentModel(data)
        add1.save()
        return 'Added student to the list'
# Create routes to list all the added students
@student.route('/students/')
def show_students():
    students = StudentModel.get_all_students()
    return render_template("students.html", students=students)
