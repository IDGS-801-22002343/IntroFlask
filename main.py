from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    titulo = "IDGS801"
    lista = ["Juan", "Carlos", "Oscar"]
    return render_template("index.html", titulo = titulo, lista = lista)

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

if __name__ == "__main__":
    app.run(debug=True, port=3000)