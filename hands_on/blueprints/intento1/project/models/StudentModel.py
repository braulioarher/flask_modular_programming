from ..extensions import db
from marshmallow import fields, Schema

class StudentModel(db.Model):
  
  #Table name
  __tablename__ = 'student'

  id = db.Column(db.Integer, primary_key=True)
  student_name = db.Column(db.String(128), nullable=False)
  student_age = db.Column(db.Integer, nullable=False)
  

  #class constructor
  def __init__(self, data):
    self.id = data.get('id')
    self.student_name = data.get('student_name')
    self.student_age= data.get('student_age')


  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all_students():
    return StudentModel.query.all()

  @staticmethod
  def get_student_id(id):
    return StudentModel.query.filter_by(id=id).first()

  def __repr(self):
      return '<id {}>'.format(self.id)


class StudentSchema(Schema):
  id = fields.Int(required=True)
  student_name= fields.Str(required=True)
  student_age = fields.Int(required=True)