# Curso Flask Modular Programming

En este curso se aprendera los siguientes temas del framework de flask:

    - Interface de linea de comandos de flask
    - Vistas basadas en clases
    - Blueprints
    - Manejo de Cookies y sesiones
    - Testing and Deployment

Tambien nos familirizaremos con el tema Template filters y Model Relationships

## Linea de comandos de Flask

En el entorno de flask un script llamado flask esta disponible el cual nos da los comandos de Flask, las extensiones y la aplicacion
Cuando se ejecuta en la terminal este muestra ek uso de la sintaxys de los scrips de flask, varias opciones de comandos estan disponibles con el

La sintaxis de un script de flask es:

        flask [options] COMMAND [ARG]

Cuando un script de flask se ejecuta con cualquier comando valido este carga la aplicacion definida en FLASK_APP con la variable de ambiente o los achivo app.py o wspi.py

Para entender como flask usa un script considerese el siguiente ejemplo escrito en hello.py presente en la carpeta project

    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def hello_view():
        return'<h1>Hello World!!</h1>'

El archivo hello.py crea la instancia flask app que tambien contiene la view function hello_view

### Comandos de flask

Estos son los siguientes comandos disponibles con flask commands:
    routes - Muestra kas rutas disponibles para la app
    run - Correl el servidor de desarrollo
    shell - Inicia a Python shell en el contexto de la aplicacion

Antes de correr cualquiera de los comandos la variable de entorno FLASK_APP se debe declarar

### Uso del comando routes

El comando routes muestra una lista de rutas disponibles para la aplicacion
El siguiente ejemplo ejecuta el comando routes y muestra una salida

        flask routes

### Uso del comando run

El comando run corre el servidor de desarrollo

    flask run

### Uso del comando shell

El comando flask shell abre la shell interactiva de Python. Automaticamente importa las instancias de la app aosciadas
La ejecusion del conado muestra una salida comi la siguiente

        $ flask shell
        Python 3.5.0 (...)...
        App: hello
        Instance: ...../project/instance
        >>> print(app)
        <Flask 'hello'>

### Agregando imports por defecto

Otra intancia aparte de app, tu tambien puedes importat otros objetos automaticamente cuando la shell carga
Esto se pude mediante el decorador shell_context_processer
El archivo hello.py se edita a continuacuin el decorador shell_contest_proceser se agrega a la funcion make_shell_context que returna un diccionarico con las llaves "app", "x" y "y"

        from flask import Flask

        app = Flask(__name__)

        @app.shell_context_processor
        def make_shell_context():
            return dict(app=app, x=25, y=65)

        @app.route('/')
        def hello_view():
            return '<h1>Hello World!!!</h1>'

Al ejecutar flask shell la salida debe ser como lo siguiete

        $ flask shell
        Python 3.5.0 (...)...
        App: hello
        Instance: ...../project/instance
        >>> print(app)
        <Flask 'hello'>
        >>> print(x)
        25
        >>> print(y)
        65

El ejemplo anterior claramaente muetra kis objetos app, x y y estos son importados al inicial la shell por su cuenta

### Crean un comando custom

Aparte de los tres comandos tu tambien puedes crear tu propio comando para esto:

        from flask import Flask
        import click

        app = Flask(__name__)

        @app.cli.command()
        @click.argument('name')
        def mycommand(name):
            print(name)

mycommand se define como una funcion que toma el argumento name
la funcion es decorada con cli.command() indicando que se anniade a la cli
ahora puedes correr mycomand desde la terminal como se muestra

        $ flask mycommand John
        John

### Agregando un Customa Command

Es posible agrupa comandos similares dentro de un simple numbre
El ejemplo mostrado agrupa con el nombre de group1 y el comando command1 se agrega a dicho grupo

        from flask import Flask
        import click
        from flask.cli import AppGroup

        app = Flask(__name__)
        group_cli = AppGroup('group1')

        @group_cli.command('command1')
        @click.argument('name')
        def mycommand(name):
            print(name)

        app.cli.add_command(group_cli)

Que a la salida nos da

        $ flask group1 command1 John
        John

## Uso de filters en los templates

Los filtros son una funciones ya incluidad que lateran el valor de las variables por proposito de como se muestran, la sitaxis para usar un filtro es la siguiente:

        {{ variable | filter_name(*arg) }}
    si el filtro no rquiere de ningun argumento entonces la sintaxis luce asi:
        {{ varible | filter_name }}

Si alguna variable no contine algun valor 'None' entonces se puede remplazar por el valor por defecto usando 'default' en el siguiente ejemplo la variable a tiene 'None' y esa muestra el mensaje 'Default Value' al usuario en el template renderizado

    {{ a | default(Default Value) }}

### Filtro int, float round

Los filtreos int, float convierten el valor de la variable a entero o flotanten respectivamente
        {{ 67.7 | int }}
        67
        {{ 75 | float }}
        75.0
        round redondea el valor a un valor flotanto con un numero especifico de decimales
        {{ 5.16725 | round }}   -> 5.0
        {{ 5.16725 | round(2) }}   -> 5.17
        {{ 5.16725 | round(2) }}   -> 5.167
        {{ 5.16725 | round(0, "floor") }}   -> 5.0
        {{ 5.16725 | round(0, "ceil") }}   -> 6.0

### Filtro join

El filtro join se usa para convina todos los elementos de una lista especificado en la variable del bloque
Cada elemento de la lista es convertido a string antes de unirse entre si
El siguiente ejeplo muestra como el filtro join funcuina cuando la lista k = [8, 15, 25, 88, 12, 78] se pasa al template

        {{ k | join(',') }} -> 8,15,25,88,12,78
        {{ k | join(',') }} -> 8-15-25-88-12-78

### Filtro length

El filtro length se usa para regresar el tamano de la variable

El siguiente ejemplo muestra el uso del filtro length de la lista k = [8, 15, 25, 88, 12, 78]

        {{ k | length }}
        6

### Chaining Filters

Loas filtros se pueden encadenar
El ejemplo a continuacion inicialmente convierte toso los caractes del string "s" a minuscular con en filtro lower
la version en minusculas es entonce convetida a titulo usando el filtro title

    {{ s | lower | title }}     -> Hello World

### Custom filters

Adicionalmente a los filtros ya incluidos es posible de crear filtros propios y usarlos en los templates
Un custom filter es una funcion regular de Python, Esta tine que ser definida inicialmente y luego anadida a la variable de entorno jinja_env.filters
El siguiente ejemplo define un custom filter en el archivo startswith in hello.py

        def startswith(word, tag):
            if word.startswith(tag):
                return tag + '-word'

            return 'non-' + tag + '-word'

        app.jinja_env.filters['startswith'] = startswith

#### Usando un custom filter

El custom filter starswith definido anteriormente verifica si un string empoeza con una specifica tag o no

Si el stringo empieza con la tag esoecificada entonce regresa \<tag>-word de la otra forma refes non-\<tag>-word

ejemplo:

        {{ 'university' | startswith('un' ) }}       ->  un-word
        {{ 'university' | startwith('pre') }}        -> non-pre-word

## Establecer relaciones entre modelos

Establecer relacion entre dos modelos permite a los objetos de un modelo que se haga referencia entre los ibjetos relacionados the otro modelo automaticamente

Al establecer la relacion entre tablas los datos pueden ser manejados efectivamente y evitar la redundancia

En este tema sabremos como establecer relaciones uno a uno, uno a muchos y muchos a muchos con los modelos en SQLAlchemy

### Relacion uno a uno

En la relacion uno a uno, un registro de la tabla esta asociado solo con un registro en la otra tabla relacionada

Para entender mejor definamos dos modelos User y Contact en un nuevo archivo llamado models.py

La relacion se establece de una manera que cada usuario tiene un contacto:

En el ejemplo de models podemos observar que el modelo User contiene un metodo llamado db.relationship este metodo toma varios argumentos

        El primer argumento se refiere al nombre del modelo con el cuan necesita establecer relcion
        El valor pasado a backref define una nueva propiedad al modelo relacionado por ejemplo Contact
        Por ejemplo, my_contact, una instancia del modelo Contact puede acceder al usuario asociado con la expresion my_contact.user
        El argumento lazy le dice SQLAlchemy cuando cargar la informacion de la base de datos
        El valor False en uselist establece una relacion uno a uno entre los modelos User y Contact
Para cargar informacion a la base de datos desde flask shell:

                >>> user1 = User(username='John Williams')
                >>> user2 = User(username='Fordo Baggings')
                >>> db.session.add(user1)
                >>> db.session.add(user2)
                >>> db.session.commit()
                >>> User.query.all()

Despues de agregar los dos usuarios para agregar el contacto a cada usuario

                [<User 'John Williams'>, <User 'Fordo Baggings'>]
                >>> user1.contact = Contact(city='London', email='john.willy@xyz.com', phonenum='675-876-2423')
                >>> user2.contact = Contact(city='Chicago', email='fbaggin@abc.com', phonenum='563-983-7682')
                >>> db.session.add(user1)
                >>> db.session.add(user2)
                >>> db.session.commit()
                >>> Contact.query.all()
                [<Contact 1>, <Contact 2>]
                >>> user1.contact.email
                'john.willy@xyz.com'
                >>> contact = Contact.query.get(2)
                >>> contact.user
                <User 'Fordo Baggings'>

Los contactos se guardan en la tabla contact cuando la sesion con la base de datos termina
Tambien se puede acceder a los contactos desde un objeto asociado a usuario y visceversa

## Relacion uno a muchos

En la relacion uno a muchos un registro de una tabla esta asociado con uno o mas registros de otra tabla
Para enteneder la este tipo de relacion considerando los dos modelos User y Blogpost definidos en models.py
En esta relacion cada blogpost se escribe por un usuario y un usuario puede tener muchos blogpost
Vamo a definir un nuevo model Blogpost y modificar el ya existente User para asi poder establecer la relacion uno a muchos entre estos dos modelos

Una ves agregados nuestro modelo Blogpost en models.py y la relacion a la tablas Users podemos anadir informacion a la tabla para esto desde flask shell:

        >>> from models import User, Blogpost
        >>> users = User.query.all()
        >>> post1 = Blogpost(title='Flask - A Python Web Framework')
        >>> post2 = Blogpost(title='Using Templates in Flask')
        >>> post3 = Blogpost(title='Working with Databases in Flask')
        >>> post4 = Blogpost(title='RestAPI Programming in Flask')
        >>> post1.userid = users[0].id
        >>> post3.userid = users[0].id
        >>> post4.userid = users[1].id
        >>> post2.userid = users[1].id
        >>> db.session.add(post1)
        >>> db.session.add(post2)
        >>> db.session.add(post3)
        >>> db.session.add(post4)
        >>> db.session.commit()

Como se muestra en la flask shell cuatro post fueron creados y dos de ellos se refieren a usuario John Williams y los dos restantes se refieren a Fordo Baggings

### Accediendo a los blog post relacionados

Los siguientes comandos ejecutados en la shell de flask muestran como acceder al los post asociados con un usuario:
Tambien mustra como acceder al objeto de usuario asociado con un blog post especifico

        >>> users[0].blogposts.all()
        [<Blogpost 'Flask - A Python Web Framework'>, <Blogpost 'Working with Databases in Flask'>]
        >>> blogposts = Blogpost.query.all()
        >>> blogposts
        [<Blogpost 'Flask - A Python Web Framework'>, <Blogpost 'Using Templates in Flask'>, <Blogpost 'Working with Databases in Flask'>, <Blogpost 'RestAPI Programming in Flask'>]
        >>> blogposts[0].user
        <User 'John Williams'>

## Relacion mucho a muchos

En la relacion mucho a muchos cualquier record de una tabla puede estar asociado a culquier recorde de la otra tabla
Para entender esta relacion vamos a considerar dos modelos Blogpost y Tag
En esta relacion cada post puede ser etiquetada a multiples etiquetas, Simila multiples posts pueden tener la misma etiqueta
Definiremos un nuevo modelo Tag y modificaremos el ya existenten BlogPost tambien definiremos una tabla de ayuda tags que se usa para monstar la relacion

Una vez definido nuestro modelo Tag y la tabla de ayuda Tags y haber creado la relacion en la tabla Blogpost podemos crear cinco objetos Tag en el entordo de la aplicacion

        >>> Tag.query.all()
        []
        >>> tag1 = Tag(tagname='Python')
        >>> tag2 = Tag(tagname='Flask')
        >>> tag3 = Tag(tagname='DB connectivity')
        >>> tag4 = Tag(tagname='Templates')
        >>> tag5 = Tag(tagname='Rest API')
        >>> db.session.add(tag1)
        >>> db.session.add(tag2)
        >>> db.session.add(tag3)
        >>> db.session.add(tag4)
        >>> db.session.add(tag5)
        >>> db.session.commit()
Ahora asociamos las etiquetas definidas para los blogpost existentes como se muestra a continuacion

        >>> blogposts = Blogpost.query.all()
        >>> blogposts[0].tags
        []
        >>> blogposts[0].tags = [tag1, tag2]
        >>> blogposts[1].tags = [tag1, tag2, tag4]
        >>> blogposts[2].tags = [tag1, tag2, tag3]
        >>> blogposts[3].tags = [tag1, tag2, tag5]
        >>> db.session.commit()
Ahora trataremos de acceder a las etiquetas asociadas con el blogpost usando el atributo tags

        >>> blogposts = Blogpost.query.all()
        >>> blogposts[0].tags
        [<Tag 'Python'>, <Tag 'Flask'>]
        >>> blogposts[3].tags
        [<Tag 'Flask'>, <Tag 'Python'>, <Tag 'Rest API'>
Se puede filtrar los blogpost con una especifica etiqueta usando el atributo blogpost
El codigo a continuacion filtra los blogpost asociadas con la etiqueta Python y Rest API

        >>> tag1 = Tag.query.get(1)
        >>> tag1.blogposts.all()
        [<Blogpost 'Flask - A Python Web Framework'>, <Blogpost 'Using Templates in Flask'>, <Blogpost 'Working with Databases in Flask'>, <Blogpost 'RestAPI Programming in Flask'>]
        >>> tag3 = Tag.query.get(3)
        >>> tag3.blogposts.all()
        [<Blogpost 'Working with Databases in Flask'>]

## Vistas basadas en clases

Hasta el momento ya hemos trabajado con views escritas como funciones, sin embargo en caso de que muchas funciones tengan las una funcionalidad similar entonce se aconseja implementar las vistas como clases. En este tema usted va a aprnede como escribir Class Based Views

La actividad mas frecuente actividad que se hace cuando renderizas un templates, el ejemplo siguiente define una clase BaseView que aceota un template_name como entrada y es capaz de renderizar, aquella funcionalidad definida bajo el metodo dispatch_request este ejemplo se puede ver en routes.py

### Manejando multiples metodos

Por defecto las view functions de una clase soportan solamente el metodo HTTP "GET"
En caso de que tenga que soportar multiples metodos HTTP los metodos se pueden especifica en la lista methods como se muestra a continuacion:

                class BaseView(View):
                methods = ['GET', 'POST']
                …
                def dispatch_request(self):
                        if request.method == ‘GET’:
                        return render_template(self.template)
                        elif request.method == ‘POST’:
                        …

Como se vio en el ejemplo el metodo dispatch_request de BaseView maneja los metodos GET y POST, el numero de condiciones if aumenta cuando los metodos HTTP a la par de que las view functions aumentan. Esto reduce lectura e incrementa la complejidad

El problema anterior se pide resolver usando la clase MethodView, cualquier clase derivada de una clase MethodView permite definir metodos seprados para manejar los metodos HTTP

El ejemplo a continuacion muestra como la clase MethodView se puede usar:

                from flask.views import MethodView

                class UserAPI(MethodView):

                def get(self, user_id):
                        ...

                def post(self):
                        ...

                def put(self, user_id):
                        ...

                def delete(self, user_id):
                        ....       
El codigo anterior define los metodos de UserAPI que son get, post, put y delete

        app.add_url_rule('/users/<int:user_id>', view_func=UserAPI.as_view('user_api'),
methods=['GET', 'PUT', 'DELETE'])

## Blueprints

En flask Blueprints se usan para desarrolar componentes de una aplicacion que soporta patrones en comun con un aplicacion o a travez de aplicaciones. Un objeto Blueprint se comporta similar a un objeto de aplicacion por lo tanto no un Blueprint no es una aplicacion y usa solo las funciones de agregar o extender a la aplicacion existente

### Usos de los Blueprints

Blueprints son generalmente usados en Flask para los siguientes propositos:

        -Organizar toda la aplicacion en componentes individuales
        -Hacer un blueprint de una aplicacion disponible solamente el prefijo especifico del URL
        -Hacer del blueprint de una aplicacion se multiplique varias veces con una variedad de URL

Se creara un blueprint en el archivo sample_blueprint.py para poner en practica lo aprendido

Una vez que se crea la funcion create_app se exporta la variable FLASK_APP a la carpeta del proyecto y se puede correr la aplicacion

## Manejando Cookies

Una cookie se refiere a enviar informacion desde un servidor web y alamcenar la inofrmacion en la computadora del cliente dentro de un archivo
El principal objetivo de las cookies es rastrear la actividad del usuario en una sitio web para mejorar la experiencia de usuario

### Cookies en Flask

En una aplicacion flask, las cookies puen ser accedidas dede un atributo de un objeto request
El atributo cookies es un diccionario que ontiene todas las variables y sus valores correspodientes que se transmiten por el cliente
Adicionalmente una cookie puede alcenar su tiempo de expiracion
En flask las cookies se pueden establecer usando el metodo set_cookie en un objeto de respuesta HTML

### Accediendo a una cookie

Por motivos de representacion dirijse a la aplicacion helloapp a routes.py

## Sesiones

Una sesion es capaz de guardar informacion especifica de un usuario en un servidor
Una sesion co un cliente obtiene una session ID
La informacion capturada durante la session se almacena en las cookies y se firma criptograficamente
Cualquier usuario puede ver la informacion de las cookies pero no las puede modificar
Pra la encriptacion se tiene que definir una secret key en la aplicacion

### Sesiones en flask

Caulquier informacion necesaria se puede  almacenar en un objeto session
Un objeto session es un diccionario que tiene pares de llaves y valor donde las variables de session se declaran como llaves
Para continuar se agrega codigo al documento config para asignar la secret key

## Probando aplicaciones de Flask

Como ya se sabe Aplication Testing es un paso importante que revida si una aplicacion se conporta como se espera basado en codigo escrito
Hay principalmente tres tipos de pruebas: Unit Testing, Integration Testing y System Testing
Unit Testing: Es una prueba que verifica que este bien las mas pequenas unidades de codigo como las funciones
Integration Testing: Revisa si lod diferentes componentes iteractuan como se espera
System Testing: Esta prueba que funcione correctamente todo el sistema

Una aplicacion flask viene con un test client el cual es capaz de simular HTML requests y regresar un objeto como respuesta
Se deben de escribit los test cases, que compruebe cada funcion con informacion cubriendo cada parte de la funcion
En este tema vamos a ver como escribir metodos de prueba para dos funciones dentro de routes.py

Inicialmente creamos una carpeta llamada tests dentro del proyecto y creamos el archivo __init__.py dentor del folder

Una vez creados nuestro archivos de pruebas podemos correr la prueba con:

        python3 -m unittest discover helloapp -v

A parte de los metodos assertEqual y assertIn, unittest tiene otros metodos assert utiles para depurar informacion algunos de estos metodos son:

assertTrue(x): Checa que x es True
assertIs(x, y): Checa si x es y
assertIsNone(x): Checa si x es None
assertNotIn(x, y): Checa si x no es parte de y
assertIsInstance(x, y): Checa si x es instancia de y

Ahora definiremos el metodo test_login que verifica la funcionalidad de la pagina /login

### Usando la extension Flask-Testing

Flask-Testing es una extension de flask que tiene mas utilidades unit testing
Al usar Flask-Testing, las clases de prueba de derivan de la clase TestCase del modulo flask_testing
El caso de prueba definidp debe que contener la definicion para el metodo create_app que regresa una instancia a la aplicacion Flask
Tambien se puede ejecutar la prueba con un servidor corriendo usando herramientas como selenium

## Desplegando una aplicacion Flask

Despues de probar exitosamente la aplicacion esta debe ser movida a produccion
Hay varias formas de hostear la aplicacion Flask
Casi todas las aplicaciones de Python corren en servidores compatibles con WSGI
Adicionalmente las aplicaciones Flask se puede hostear en Plataform-ad-a-Servis (Paas) en plataformas como Heroki, Amazon web Services y Google Cloud
En este ejemplo veremos a grandes razgos como desplegar la aplicacion Flask en algunos servidores WSGI independientes en la plataforma Heroku

### Desplegando en Gevent

Gevent is una libreria basada en corutinas de Python, tiene una interfaz simple que corre aplicaciones WSGI
Para desplegar el proyecto se creara un archivo gserver.py en la carpeta del proyecto:
from gevent.pywsgi import WSGIServer
from helloapp import create_app

app = create_app()

server = WSGIServer(('', 5000), app)
server.serve_forever()

ahora podemo ejecutar el comando python3 gserver.py

Una vez creado el archivo podemos correr el comando para activar correr la aplicacion:

        python3 gserver.py

### Desplegando en Gunicorn

Gunicorn es un servidor HTTP WSGI para unix
Adicionalmente a otros servidores web Python, tiene una buena interfaz de usuario que es facil de usar y configurar
Para desplegar el projecto se debe de crear los archivos wsgi.py en el proyecto

from project import create_app

app = create_app()

agregamos las lineas anteriores y corremos el comando para correr el servidor

gunicorn -w 4 myproject.wsgi:app

### Desplegando en uWSGI

uWSGI se usa como servidor de aplicacion para muchos lenguajes de programacion incluyendo python
uWSGI puede se puede correr como un servidor independiente o como un servidor web completo como Nginx o apache
Similar como se uso con Gunicorn el archivo wsgi.py debe ser creado
from project import create_app

app = create_app()
para correr el servidor se usa el comando

En lugar de usar las opciones de linea de comandos, se puede especificar las opciones en un nuevoarchivo uwsgi.ini como se muestra a continuacion y entonces usar el comando uwsgi uwsgi.ini

[uwsgi]
socket = 127.0.0.1:8080
wsgi-file = wsgi.py
callable = app
processes = 6
threads = 3

### Desplegando con Nginx y uWSGI

En caso de que esperemos mejor performance de la aplicacion web, se recomienda usar un servidor web como Nginx para el front end para servir a un servidor WSGI como uWSGI usando un reverse proxy
Se necesita crear un archivo ngnix.conf con uwsgi.ini como se mostro ateriormente y poner ambos archivos en la carpeta etc/nginx/sites-available/directory
las configuranciones ngnix,conf son similares a las siguientes

Archivo nginx.conf:

server {
    listen 8000;
    server_name 127.0.0.1;

    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:8081;
    }
    
    location /static {
        alias /home/deploy/project/static;
    }
}

Archivo uwsgi.ini:

[uwsgi]
http = 127.0.0.1:8081
wsgi-file = wsgi.py
callable = app
processes = 4
threads = 2

Las configurancione ateriores le dicen a Ngnix que escuhe a las peticiones de entrada en el puerto 8000 y redirija todas las peticiones WSGI a la aplicacion en el puerto 8081
Tambien hace una ecepcion para las peticiones de archivos estaticos

Una vez creados los archivos anteriores nos dirigimos a la carpeta /etc/nginx/sites-enabled para crear un link simbolico el cual apuntara a nuestro archivo creado en etc/nginx/sites-available/ para esto:
        sudo ln -s /etc/nginx/sites-available/deploy.conf .

Una vez echo esto podemo reiciar el servidor con los comandos:

                sudo service nginx restart
                        o
                sudo nginx -s reload

echo lo anterir entonces podemos ejecutar el comando desde nuestro entorno virtual:

         uwsgi uwsgi.ini

Ahora ya podemos entrar a las direcciones 172.0.0.1:8000/ y 172.0.0.1:8081/ y obtendremos la misma respuesta

### Desplegando en Heroku

Heroku is una Paas. Una aplicacion basada en Heroku funciona en base a comandos escritos en Procfile
Estos comandos se corren por Heroku dyno por ejemplo en una maquina virtual
Por lo tanto crear un archivo Procfile en el directorio de nivel superir del proyecto y anadir el contenido abajo

### Resumen del curso

En este curso hemos analizado los siguientes temas:

        -Introduccion a la linea de comandos de Flask creando nuevos comandos y anadiendolos a la linea de comandos
        -Desarrollar filtros personalizados para usarse en templates
        -Establecer relaciones uno a uno, uno a muchos y muchos a muchos a travez de los modelos
        -Usar vistas basadas en clases
        -Crear blueprints
        -Manejar cookies y sesiones
        -Probar las aplicaciones Flask 
        -Desplegar la aplicacion Flask
