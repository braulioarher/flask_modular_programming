import pytest
from project import app, db
import json
import base64
from flask import Flask
import os
from project.models import StudentModel
from project.models import TeacherModel

class Test_API:
	client  = app.test_client()
	
	@pytest.fixture(autouse=True, scope='session')
	def setUp(self):
		app.config['TESTING'] = True
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db'
		db.create_all()
		yield db
		os.remove('testing.db')

	def test_student_in_db(self):
		result  = StudentModel.query.all()
		assert len(result) == 0
		assert result == []

	def test_students_list(self):
		url = "api/students/"
		response = self.client.get(url)
		assert response.status_code == 200
		assert response.json == []

	def test_students_register_method(self):
		url = "/api/students/add"
		payload = '{"id": 1,"student_age": 16 , "student_name": "testname"}'
		headers = { 'Content-Type': "application/json",  'cache-control': "no-cache"  }
		response = self.client.post(url, data=payload, headers=headers)
		assert response.status_code == 201
		assert response.json['message'] == 'Added student to the list'
		
	
	def test_data_in_db_after_adding(self):
		result  = StudentModel.query.all()
		assert len(result) == 1
		assert result[0].student_name == 'testname'


	def test_after_adding_students(self):
		url = "api/students/"
		response = self.client.get(url)
		assert response.status_code == 200
		assert response.json == [{'id': 1, 'student_age': 16, 'student_name': 'testname'}]		

	def test_teachers_in_db(self):
		result  = TeacherModel.query.all()
		assert len(result) == 0
		assert result == []
	
	def test_teachers_list(self):
		url = "api/teachers/"
		response = self.client.get(url)
		assert response.status_code == 200
		assert response.json == []

	def test_teachers_register_method(self):
		url = "/api/teachers/add"
		payload = '{"id": 1,"teacher_subject": "maths" , "teacher_name": "testteacher"}'
		headers = { 'Content-Type': "application/json",  'cache-control': "no-cache"  }
		response = self.client.post(url, data=payload, headers=headers)
		assert response.status_code == 201
		assert response.json['message'] == 'Added teacher to the list'
			

	def test_data_in_db_for_teachers(self):
		result  = TeacherModel.query.all()
		assert len(result) == 1
		assert result[0].teacher_name == 'testteacher'
		assert result[0].teacher_subject == 'maths'


	def test_after_adding_teachers(self):
		url = "api/teachers/"
		response = self.client.get(url)
		assert response.status_code == 200
		assert response.json == [{'id': 1, 'teacher_name': 'testteacher', 'teacher_subject': 'maths'}
]		
