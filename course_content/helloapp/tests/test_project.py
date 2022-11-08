import unittest
from urllib import response

from helloapp import create_app
from helloapp.models import db, User


#Definimos un caso de prueba TestURLs que se deriva de unittest.TestCase
class TestURLs(unittest.TestCase):
    #Estas lineas corren antes de ejecutar cualquier metodo de la prueba
    #Se crea un instancia a la aplicacion para disponer del cliente con la variable self.client
    def setUp(self):
        app = create_app({
            'TESTING' : True,
            'SQLALCHEMY_DATAPASE_URI' : 'SQLITE:///tests\\test_database.db'
        })
        self.client = app.test_client()
        db.app = app
        db.create_all()

    #Estas lineas se ejecutan despues de que se completa cualquier metodo de prueba disponible
    # en TestURLs
    #aqui el metodo tearDown elimina todas las sesiones de la base de datos y elimina las tablas
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    #El metodo get accede a la direccion URL especificada como argumento y regresa una respuesta
    # HTML que se guarda en el objeto response
    #El status code esperado del objeto response se verifica con el atributo status_code usando
    # el metodo assertEqual
    #Similar, el metodo assertIn verifica si Hello World!!! esta presente en objeto response.data
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello World!!!", response.data)

    #Este metodo verifica la funcionalidad de la pagina /login
    #El metodo de prueba hace un post con la informacion requerida especificada como un
    #diccionario al argumento data del metodo post
    #el argumento follow_redirects se pone en True porque la vista login redirecciona
    #a la pagina hello.index despues de un login exitoso
    def test_login(self):
        response = self.client.post('/login', data=dict(username='Sample User'), follow_redirect=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Logged in as Sample User", response.data)

# para ejecutar la prueba desde la consola:

    #   python3 -m unittest discover helloapp -v