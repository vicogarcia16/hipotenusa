from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import numpy as np

app = Flask(__name__)
Bootstrap(app)

def calcular_hipotenusa(cateto1, cateto2):
    """Calcula la hipotenusa dado los dos catetos."""
    return np.sqrt(cateto1**2 + cateto2**2)

def calcular_cateto2(cateto1, hipotenusa):
    """Calcula el cateto2 dado el cateto1 y la hipotenusa."""
    return np.sqrt(hipotenusa**2 - cateto1**2)

def calcular_cateto1(cateto2, hipotenusa):
    """Calcula el cateto1 dado el cateto2 y la hipotenusa."""
    return np.sqrt(hipotenusa**2 - cateto2**2)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado_option = None
    resultado_cateto1 = None
    resultado_cateto2 = None
    resultado_hipotenusa = None

    if request.method == "POST":
        opcion = request.form.get("opcion")
        resultado_option = opcion

        if opcion == "1":
            cateto1 = float(request.form.get("cateto1", 0))
            cateto2 = float(request.form.get("cateto2", 0))
            resultado_hipotenusa = calcular_hipotenusa(cateto1, cateto2)

        elif opcion == "2":
            cateto2 = float(request.form.get("cateto2", 0))
            hipotenusa = float(request.form.get("hipotenusa", 0))
            resultado_cateto1 = calcular_cateto1(cateto2, hipotenusa)

        elif opcion == "3":
            cateto1 = float(request.form.get("cateto1", 0))
            hipotenusa = float(request.form.get("hipotenusa", 0))
            resultado_cateto2 = calcular_cateto2(cateto1, hipotenusa)

    return render_template("index.html", resultado_option = resultado_option, resultado_cateto1=resultado_cateto1,
                           resultado_cateto2=resultado_cateto2, resultado_hipotenusa=resultado_hipotenusa)

if __name__ == "__main__":
    app.run(debug=True)
