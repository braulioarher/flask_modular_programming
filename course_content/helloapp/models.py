from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))
    contact = db.relationship(
        'Contact',
        backref='user',
        lazy=True,
        uselist=False
    )
    blogposts = db.relationship('Blogpost', backref='user', lazy='dynamic')
    # El valor de lazy se establece como dynamic el cual regresa una consulta objeto,
    # la cual puede ser redefinida antes de cargar la informacion

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User '{}'>".format(self.username)

class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    city = db.Column(db.String(200))
    email = db.Column(db.String(100))
    phoneno = db.Column(db.String())
    userid = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)

    def __init__(self, city, email, phonenum):
        self.city = city
        self.email = email
        self.phoneno = phonenum
    #Esta clase contiene la columna llamada userid que establece la relacion con el id de la 
    # tabla user
    #La columna userid contiene la Foreign Key Constraint y esta no puede ser null
    
#Ahora definimos una tabla de ayuda llamada tags con el siguiente contenido
tags = db.Table('blogpost_tags',
db.Column('blogpost_id', db.Integer, db.ForeignKey('blogpost.id')),
db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)
# tags definido arriba no es un modelo es una tabla
# Una tabla de ayuda se usa cuando no se requiere acceder a filas individuales
# Cada fila de la tabla de ayuda contiene una o mas filas una de la tabla blogpost que se 
# identifica por blogpost_id y otra de la tabla tag que se identifica por tag_id

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    text = db.Column(db.Text())
    pubish_date = db.Column(db.DateTime())
    userid = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    tags = db.relationship('Tag', secondary=tags, backref=db.backref('blogposts', lazy='dynamic'))
    # En la definicion anterior db.relationship toma un argumeto secondary y su valor
    # se asigna a tags
    # Lo anterior le dice a SQLAlchemy que la relacion se almacena en la tabla de ayuda tags

    def __init__(self, title):
        self.title = title
    def __repr__(self):
        return f"<Blogpost {self.title}>"
    # En este ajemplo la columna userid contiene la Foreign Key Constraint y no puede ser nulo
    # Esto asegura todos los blogpost se refieren a un usuario
    # La definicion de la columna userid usa el valor 

class Tag(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    tagname = db.Column(db.String(255))

    def __init__(self, tagname):
        self.tagname = tagname
    def __repr__(self):
        return f"<Tag> {self.tagname}"
    # No se establece ninguna relacion en este modelo

