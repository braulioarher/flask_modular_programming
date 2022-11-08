import requests

client = 'http://127.0.0.1:5000/api/students/add'

payload = '{"id": 5,"student_age": 22 , "student_name": "Jaesus"}'
headers = { 'Content-Type': "application/json",  'cache-control': "no-cache"  }
#response = requests.get(client)

x = requests.post(client, data=payload, headers=headers)
print(x.text)