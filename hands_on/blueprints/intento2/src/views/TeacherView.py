from flask import request, json, Response, Blueprint
from flask import render_template
from flask_cors import CORS, cross_origin
from ..models.TeacherModel import TeacherModel, TeacherSchema

#Add your code here
teacher = Blueprint(
    'teachers',
    __name__,
    )
teacher_schema = TeacherSchema()

# Create routes to add a teacher to the database.
@teacher.route('/add', methods=['POST'])
def create_teacher():
    req_data = request.get_json()
    data = teacher_schema.load(req_data)

    teacher = TeacherModel(data)
    teacher.save()

    resp_data = teacher_schema.dumps(teacher)
    message = {'message': 'Added teacher to the list'}
    return Response(mimetype="application/json", response=json.dumps(message), status=201)
# Create routes to list all the added teachers
@teacher.route('/')
def show_teachers():
    teachers = TeacherModel.query.all()
    resp = teacher_schema.dump(teachers, many=True)
    return Response(mimetype="application/json", response=json.dumps(resp), status=200)