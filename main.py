from flask import Flask, render_template, request
from datetime import datetime
import forms
from flask import g
from flask import flash
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = "esta es una clave secreta"
csrf = CSRFProtect()


@app.errorhandler(404)
def page_notfound(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.user = "Mario"
    print("before 1")


@app.after_request
def after_request(response):
    print("after 1")
    return response

@app.route("/")
def index():
    nom = "None"
    titulo = "IDGS801"
    lista = ["Juan", "Carlos", "Oscar"]
    nom = g.user
    print("Index 2 {}".format(g.user))
    return render_template("index.html", titulo = titulo, nom = nom, lista = lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")


@app.route("/hola")
def hola():
    return "<h1>Hola, Mundo -- Hola!<h1>"


@app.route("/user/<string:user>")
def user(user):
    return f"<h1>Hola, {user}<h1>"


@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>El numero es, {n}<h1>"


@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"<h1>Hola, {username}! Tu ID es: {id}<h1>"


@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"<h1>La Suma es, {n1 + n2}<h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param = "Juan"):
    return f"<h1>Hola, {param}<h1>"

@app.route("/operas")
def operas():
    return '''
                <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="name">apaterno:</label>
        <input type="text" id="name" name="name" required>
               </form>
            '''

@app.route("/OperasBas")
def operasbas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods = ["POST"])
def result():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    operacion = request.form.get("operacion")

    if operacion == "suma":
        resultado = int(n1) + int(n2)
        simbolo = "+"
    elif operacion == "resta":
        resultado = int(n1) - int(n2)
        simbolo = "-"
    elif operacion == "multiplicacion":
        resultado = int(n1) * int(n2)
        simbolo = "x"
    elif operacion == "division":
        resultado = int(n1) / int(n2)
        simbolo = "/"
    
    return render_template("OperasBas.html", res = resultado, num1 = n1, num2 = n2, simb = simbolo)



@app.route("/Cinepolis")
def cinepolis():
    return render_template("cinepolis.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    nombre = request.form.get("nombre")
    personas = int(request.form.get("personas"))
    boletos = int(request.form.get("boletos"))
    cineco = request.form.get("cineco") == "si"
    
    
    limite = 7 * personas
    if boletos > limite:
        mensaje = "Error: No puedes comprar mas de {} boletos".format(limite)
        return render_template("cinepolis.html", mensaje=mensaje)

    precio_unitario = 12
    descuento1 = 0.10  
    descuento2 = 0.15  
    descuento_cineco = 0.10 
 
    total = boletos * precio_unitario

    if 3 <= boletos <= 5:
        total *= (1 - descuento1)
    elif boletos > 5:
        total *= (1 - descuento2)

    if cineco:
        total *= (1 - descuento_cineco)

    return render_template("Cinepolis.html", total=total, nombre=nombre, boletos=boletos, mensaje=None)


def obtener_signo_zodiaco_chino(anio):
    signos = ["Mono", "Gallo", "Perro", "Cerdo", "Rata", "Buey", "Tigre", "Conejo", "Dragon", "Serpiente", "Caballo", "Cabra"]
    
    while anio >= 12:  
        anio -= 12  

    return signos[anio]


@app.route("/Zodiaco")
def zodiaco():
    return render_template("zodiaco.html")

@app.route("/signo", methods=["POST"])
def obtenerSigno():
    nombre = request.form.get("nombre")
    apellido_paterno = request.form.get("apellido_paterno")
    apellido_materno = request.form.get("apellido_materno")
    dia = int(request.form.get("dia"))
    mes = int(request.form.get("mes"))
    anio = int(request.form.get("anio"))
    sexo = request.form.get("sexo")
    
    fecha_actual = datetime.now()

    edad = datetime.now().year - anio

    if (mes > fecha_actual.month) or (mes == fecha_actual.month and dia > fecha_actual.day):
        edad -= 1
        
    signo = obtener_signo_zodiaco_chino(anio) 
    
    return render_template("zodiaco.html", nombre=nombre, apellido_paterno=apellido_paterno, apellido_materno=apellido_materno, edad=edad, signo=signo,sexo=sexo)


@app.route("/Alumnos", methods = ["GET" , "POST"])
def alumnos():
    mat = 'x    '
    nom = ''
    ap = ''
    email = ''

    alumno_clas = forms.UserForm(request.form)

    if request.method == "POST" and alumno_clas.validate():
        mat = alumno_clas.mat.data
        nom = alumno_clas.nom.data
        ap = alumno_clas.ap.data
        email = alumno_clas.correo.data

        mensaje = 'BIENVENIDO {}'.format(nom)
        flash(mensaje)

    return render_template("Alumnos.html", form = alumno_clas, mat = mat, nom = nom, ap = ap, correo = email)

@app.route("/ZodiacoChino", methods=["GET", "POST"])
def zodiacoChino():

    nombre = ""
    apellido_paterno = ""
    apellido_materno = ""
    edad = ""
    signo = ""
    sexo = ""
    mensaje = ''
    
    formZ = forms.ZodiacoForm(request.form)
    
    if request.method == "POST" and formZ.validate():
        nombre = formZ.nombre.data
        apellido_paterno = formZ.apellido_paterno.data
        apellido_materno = formZ.apellido_materno.data
        dia = formZ.dia.data
        mes = formZ.mes.data
        anio = formZ.anio.data
        sexo = formZ.sexo.data
        fecha_actual = datetime.now()
        edad = fecha_actual.year - anio - ((mes, dia) > (fecha_actual.month, fecha_actual.day))
        signo = obtener_signo_zodiaco_chino(anio)

        mensaje = 'BIENVENIDO {}'.format(nombre)
        flash(mensaje)

    return render_template("zodiacoChino.html", form=formZ, nombre=nombre, apellido_paterno=apellido_paterno, apellido_materno=apellido_materno, edad=edad, signo=signo,sexo=sexo,mensaje = mensaje)


if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)