from flask import Blueprint, render_template

sampleBP = Blueprint(
    'sample',
    __name__,
    template_folder ='templates/sample',
    static_folder= 'static/sample',
    url_prefix="/sample"
)
@sampleBP.route('/')
def home():
    return render_template('home.html')

#La clase Blueprint toma dos argumentos, el primero es el nombre del blueprint
#y el segundo es el nombre del paquete
#Los otros parametros como template_folder, static_folder son opcionales estos especifican
# donde el blueprint definido va buscar los archivos
#El argumento url_prefix tambien es opcional, el valor pasado al argumento url_prefix se anade
#automaticamente para inicial todas las rutas definidas en el blueprint