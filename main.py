from flask import Flask, render_template

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



if __name__ == "__main__":
    app.run(debug=True, port=3000)