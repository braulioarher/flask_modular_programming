from flask import Flask

app = Flask(__name__)

from myflaskproj import projectapp

from myflaskproj.filters import evenFilter

app.jinja_env.filters['evenFilter'] = evenFilter  