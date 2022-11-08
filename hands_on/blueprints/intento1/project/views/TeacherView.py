from flask import request, json, Response, Blueprint
from flask import render_template
from flask_cors import CORS, cross_origin
from ..models.TeacherModel import TeacherModel, TeacherSchema

#Add your code here
teacher = Blueprint('teacer', __name__)
# Create routes to add a teacher to the database.a
@teacher.route('/teachers/add/', methods=["POST"])
def add_teacher():
    if request.method == 'POST':
        #Se adquiere la informacion del request esta llega en formatp json
        info = request.data
        #Se interpreta el json y se como un diccionario
        data = json.loads(info)
        #Se crea una instancia un objetp para registar dato
        record = TeacherModel(data)
        record.save()
        return ('Added teacher to the list')
# Create routes to list all the added teachers.
@teacher.route('/teachers/')
def show_teachers():
    teachers = TeacherModel.get_all_teachers()
    return render_template('teachers.html', teachers=teachers)
