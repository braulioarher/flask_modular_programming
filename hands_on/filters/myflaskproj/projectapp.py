from flask import render_template
from myflaskproj import app

@app.route('/')
def hello():
    return '<h1>Welcome to MyFlaskProj </h1>'


@app.route('/access_pydatatypes/')
def accessing_python_datatypes():

    sample_data = {'str': 'Sample String',
                   'int': 56,
                   'float': 8.9,
                   'list':['John', 'Priya', 'Rosy', 'Smith'],
                   'tuple':('John', 'Priya', 'Rosy', 'Smith'),
                   'dict':{'id':'E001', 'name':'Williams', 'email':'willy@abc.com', 'city':'New York'},
                   'set' :{'Cricket', 'Basket Ball', 'Tennis', 'Foot Ball'},
                   'bool':True,
                   'none':None,
                   }

    return render_template('accessingPythonDataTypes.html',data=sample_data)


@app.route('/filters/')
def using_filters():

    sample_data = {'round':99.2,
                   'dictsort':{'John':188.976, 'Priya':170.688, 'Rosy':176.784, 'Akbar':155.7528},
                   'map':['HELLO', 'WORLD!!!'],
                   'replace' :'old is gold',
                   'tojson':[{'name':'John', 'height':188.976},
                             {'name':'Priya', 'height':170.688},
                             {'name':'Rosy', 'height':176.784},
                             {'name':'Akbar', 'height':155.7528}
                             ],
                   'evenfilter':[78, 45, 22, 9, 54, 68]
                   }

    return render_template('usingfilters.html', data=sample_data)  