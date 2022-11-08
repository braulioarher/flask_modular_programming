from ..extensions import db
from marshmallow import fields, Schema


class TeacherModel(db.Model):

  #Table name
  __tablename__ = 'teacher'

  id = db.Column(db.Integer, primary_key=True)
  teacher_name = db.Column(db.String(128), nullable=False)
  teacher_subject = db.Column(db.String(128), nullable=False)

  #class constructor
  def __init__(self, data):
    self.id = data.get('id')
    self.teacher_name = data.get('teacher_name')
    self.teacher_subject = data.get('teacher_subject')
    


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
  def get_all_teachers():
    return TeacherModel.query.all()

  @staticmethod
  def get_teacher_by_id(id):
    return TeahcerModel.query.filter_by(id=id).first()

  def __repr(self):
      return '<id {}>'.format(self.id)


class TeacherSchema(Schema):
  id = fields.Int(required=True)
  teacher_name = fields.Str(required=True)
  teacher_subject = fields.Str(required=True)