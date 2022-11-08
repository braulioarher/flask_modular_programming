from flask import Flask, request 


app = Flask(__name__)
app.secret_key = "Thisisyoursecret"


# Create a simple endpoint /Hello with return message "Welcome to your flask application"
@app.route('/Hello')
def hello():
  return ("Welcome to your flask application")

