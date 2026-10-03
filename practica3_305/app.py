from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def inicio():
    return redirect(url_for('calcular_area'))  

@app.route("/Area", methods=["GET", "POST"])
def calcular_area():
    area = None

    if request.method == "POST":
        largo = float(request.form["largo"])
        ancho = float(request.form["ancho"])
        area = largo * ancho

    return render_template('Area.html', area=area)

@app.route("/Perimetro", methods=["GET", "POST"])
def calcular_perimetro():
    perimetro = None

    if request.method == "POST":
        largo = float(request.form["largo"])
        ancho = float(request.form["ancho"])
        perimetro = 2 * (largo + ancho)

    return render_template('Perimetro.html', perimetro=perimetro)

if __name__ == "__main__":
    app.run(debug=True)