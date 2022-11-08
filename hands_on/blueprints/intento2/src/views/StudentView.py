from flask import jsonify, request, json, Response, Blueprint
from flask import render_template
from flask_cors import CORS, cross_origin
from ..models.StudentModel import StudentModel, StudentSchema

#Add your code here
student = Blueprint(
    'students',
    __name__,
    )
student_schema = StudentSchema()

# Create routes to add a student to the database.
@student.route('/add', methods=['POST'])
def create_student():
    #Guardamos el json proveniente del POST request
    req_data = request.get_json()
    #Cargamos la informacion proveniete de json para y obtenemos un diccionario
    data = student_schema.load(req_data)
    #Se pasa el diccionario con la informacion y se guarda en la base de datos
    student = StudentModel(data)
    student.save()
    message = {'message': 'Added student to the list'}
    #Regresamos una respuesta de tipo json y con status code 201
    return Response(mimetype="application/json", response=json.dumps(message), status=201)
# Create routes to list all the added students
@student.route('/')
def show_students():
    #Usamos el metodo statico get_all_students() para cargar la informacion de la BD
    students = StudentModel.get_all_students()
    #Convertirmos la informacion 
    resp = student_schema.dump(students, many=True)
    return Response(mimetype="application/json", response=json.dumps(resp), status=200)

