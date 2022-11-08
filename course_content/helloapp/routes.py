from crypt import methods
from flask import Flask
from flask import Blueprint, render_template, request, make_response, session, url_for, redirect
from .models import User
import click
from flask.views import View
from helloapp.sample_blueprint import sampleBP
from helloapp import db

app = Flask(__name__)

#Declaramos una blueprint llamada hello 
#La cual la usaremos pra decorar todas las view functions con helloBP en lugar de app.route
#Usa la funcion helloBP.add_app_template_filter para anadir starwith custom
helloBP = Blueprint(
    'hello',
    __name__,
    template_folder='templates'
)

@helloBP.route('/')
def hello_view():
    return '<h1>Hello World!!!</h1>'

#Se define la vista de index
#Esta checja si el usuario esta presente en el objeto sesion y correspondientemente
#muestra un mensaje al usuario
@helloBP.route('/index/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'> click here to log out</a></b>"
    return "You are not logget in <br><a href = '/login'><b>" + "click here to log in</b></a>"

@helloBP.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        user = User(request.form['username'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('hello.index'))
    return '''
    <form action="" method="post">
        <p>User Name : <input type='text' name='username'/></p>
        <p><input type='submit' value='Login'/></p>
    </form>
    '''

#Esta funcion elimina la sesion username del objeto session
@helloBP.route('/logout')
def logout():
    #remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('hello.index'))

#Se declara esta funcion para obtener la cookie usercount
@helloBP.route('/getcookie/')
def getcookie():
    usercount = request.cookies.get('usercount')
    return (f"Values of 'usercount' is : {usercount}")

# Se declara la siguiente funcion para establecer la cookie usercount
# Si tratamos de acceder al URL /setcookie este establece el numero de usuarioas a usercount
@helloBP.route('/setcookie/')
def setcookie():
    nusers = User.query.count()
    resp = make_response("<h2>'usercount' cookie is sucessfully set.</h2>")
    resp.set_cookie('usercount', str(nusers))
    return resp

#En este ejemplo se define una clase llamada BaseView que acepta un template_name como entrada
#y es cpaz de renderizar el template cuya funcionalidad es definida 
# en el metodo dispatch_request
class BaseView(View):
    def __init__(self, template_name):
        self.template = template_name
        super(BaseView, self).__init__()

    def dispatch_request(self):
        return render_template(self.template)

#Una regla se puede agregar usando la funcion app.add_url_rule
#Esta funcion anade una futa a la funcion llamada
#El primer argumento define la ruta y el argumento view_func toma la view function como valor
#que maneha la ruta
#La expresion BaseView.as_view tranforma BaseView en una view function
# El nombre la da view dunction se pasa como primer argumento a la funcion as_view
#El argumento restante se pasa al metodo __init__ de la clas BaseView
app.add_url_rule('/users/', view_func=BaseView.as_view('display_users', template_name='listusers.html'))

# Ahora crearemos una nueva clase llamada ListView en routes.py que podra ser usada para
# mostrar todos los elementos presentes en una tabla
# La clase ListView toma template_name y model como entrada y regresa la informacion del modelo
# usando el metodo get_objects
# Finalmente el metodo dispatch_request se define para renderizar el template con la informacion
# obtenida del modelo
class ListView(BaseView):
    def __init__(self, template_name, model):
        self.model = model
        super(ListView, self).__init__(template_name)

    def get_objects(self):
        objects = self.model.query.all()
        return {self.model.__tablename__+'s':objects}
    
    def dispatch_request(self):
        return render_template(self.template, **self.get_objects())

# Ahora agregaremos la ruta /userlist/
app.add_url_rule('/userlist/', view_func=ListView.as_view('show_users', template_name='listusers.html', model=User))

#Una vez creado el blueprint sampleBP se registra en la aplicacion
#Para esto se usa el metodo app.register_blueprint
app.register_blueprint(sampleBP)
#ahora podemos entar a 127.0.0.1:5000/sample/
#Como el URL tiene el prefijo /sample, la solicitud se dirigira a la view function inicial
#definida en sample_blueprint.py
