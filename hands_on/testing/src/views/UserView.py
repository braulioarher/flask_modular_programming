from flask import request, json, Response, Blueprint
from ..models.UserModel import UserModel, UserSchema

user_api = Blueprint('users', __name__)
user_schema = UserSchema()


@user_api.route('/add', methods=['POST'])
def create():
  req_data = request.get_json()
  data = user_schema.load(req_data)

  user = UserModel(data)
  user.save()

  resp_data = user_schema.dumps(user)
  message = {'message': 'Added user to the list'}
  return custom_response(message ,201)
  
@user_api.route('/', methods=['GET'])
def get_all():
  users = UserModel.get_all_users()
  resp = user_schema.dump(users, many=True)
  return custom_response(resp, 200)

@user_api.route('/<int:id>', methods=['GET'])
def get_one_user(id):
  user = UserModel.get_user_by_id(id)
  resp = user_schema.dump(user)
  return custom_response(resp, 200)

@user_api.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
  user = UserModel.get_user_by_id(id)
  if user!= None:
    user.delete()
    return custom_response({"message":"Deleted user"}, 204)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )
