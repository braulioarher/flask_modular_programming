from flask import Flask
from .models import db
from flask_migrate import Migrate
from .config import Config
from .commands import mycommand, group_cli

def create_app(test_config=None):

    app = Flask(__name__)
    app.config.from_object(Config)

    #migrate = Migrate(app, db)

    db.app = app
    db.init_app(app)
    
    @app.shell_context_processor
    def make_shell_context():
        return dict(app=app, db=db)

    with app.app_context():
        from .models import User, Contact, Blogpost, Tag
        db.create_all()

        app.cli.add_command(mycommand)
        app.cli.add_command(group_cli)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    from . import routes, sample_blueprint

    app.register_blueprint(routes.helloBP)
    app.register_blueprint(sample_blueprint.sampleBP)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, AppFactory'
    return app

# La funcion create_app inicializa la aplicacion app, define las configuraciones por defecto
# para app y se asocia con la base de datos
# La lineas debajo de app_context se ejecutan para ajustar ka informacion que esta 
# disponible en las actividades de la instancia de la aplicacion
# create_app registra ademas los blueprints: hello y sample_blueprint
# tambien se define una view function hello que verifica si la app corre o no
# Finalmente, la funcion create_app regresa la aplicacion flask app 
