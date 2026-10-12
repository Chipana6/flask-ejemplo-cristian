from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# ---------- Datos de ejemplo ----------
ESTUDIANTES = [
    {"id": 1, "nombre": "Cristian Chipana",   "edad": 22, "carrera": "Ing. Sistemas",   "email": "cristian@example.com"},
    {"id": 2, "nombre": "María López",        "edad": 20, "carrera": "Ing. Industrial", "email": "maria@example.com"},
    {"id": 3, "nombre": "Juan Pérez",         "edad": 21, "carrera": "Ing. Civil",      "email": "juan@example.com"},
    {"id": 4, "nombre": "Ana Rojas",          "edad": 23, "carrera": "Ing. Comercial",  "email": "ana@example.com"},
    {"id": 5, "nombre": "Luis Mamani",        "edad": 19, "carrera": "Ing. Sistemas",   "email": "luis@example.com"},
]

# ---------- Rutas ----------
@app.route("/")
def inicio():
    return render_template("inicio.html", titulo="Inicio")

@app.route("/estudiantes")
def estudiantes():
    return render_template("estudiantes.html", titulo="Estudiantes", estudiantes=ESTUDIANTES)

@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    mensaje = None
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        email = request.form.get("email", "").strip()
        asunto = request.form.get("asunto", "").strip()
        if nombre and email and asunto:
            mensaje = f"✅ Gracias {nombre}, hemos recibido tu mensaje sobre '{asunto}'."
        else:
            mensaje = "⚠️ Completa todos los campos."
    return render_template("contacto.html", titulo="Contacto", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)