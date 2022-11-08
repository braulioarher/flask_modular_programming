import requests

client = 'http://127.0.0.1:5000/api/students/add'

payload = '{"id": 3,"student_age": 16 , "student_name": "testname"}'
headers = { 'Content-Type': "application/json",  'cache-control': "no-cache"  }
response = requests.post(client, data=payload, headers=headers)
print(response.status_code)
print(response.json['message'])
