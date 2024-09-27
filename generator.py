from flask import Flask, render_template, request, send_file
import barcode
from barcode.writer import ImageWriter
import os

app = Flask(__name__)

# Ruta de almacenamiento de los códigos de barras generados
CARPETA_IMAGENES = os.path.join('static', 'images')
if not os.path.exists(CARPETA_IMAGENES):
    os.makedirs(CARPETA_IMAGENES)

# Función para generar el código de barras
def generar_codigo_barras(numero_serie):
    code128 = barcode.get_barcode_class('code128')
    codigo_barras = code128(numero_serie, writer=ImageWriter())
    
    # Guardar el archivo sin la extensión .png (Flask la añade automáticamente)
    filepath = os.path.join(CARPETA_IMAGENES, numero_serie)
    codigo_barras.save(filepath)
    
    # Devolver el nombre del archivo con la extensión .png
    return f"{numero_serie}.png"

# Ruta principal para mostrar la página con el formulario
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        numero_serie_completo = request.form["numero_serie"]
        
        # Extraer los últimos 8 caracteres del número de serie completo
        numero_serie = numero_serie_completo[-8:]
        
        # Generar el código de barras
        filename = generar_codigo_barras(numero_serie)
        
        # Redirigir a la página para mostrar el código de barras generado
        return render_template("index.html", imagen_codigo=filename, numero_serie=numero_serie)
    
    return render_template("index.html")

# Ruta para descargar el código de barras
@app.route("/descargar/<filename>")
def descargar(filename):
    filepath = os.path.join(CARPETA_IMAGENES, filename)
    return send_file(filepath, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)