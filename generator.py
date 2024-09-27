from barcode import Code128
from barcode.writer import ImageWriter
import os

def generar_codigo_barras(numero_serie):
    # Extraer los últimos 8 caracteres
    numero_serie_corto = numero_serie[-8:]
    
    # Ruta de almacenamiento de los códigos de barras generados
    carpeta_imagenes = os.path.join('static', 'images')
    if not os.path.exists(carpeta_imagenes):
        os.makedirs(carpeta_imagenes)
    
    # Generar el código de barras
    codigo_barras = Code128(numero_serie_corto, writer=ImageWriter())
    filepath = os.path.join(carpeta_imagenes, f"{numero_serie_corto}.png")
    
    # Guardar el archivo
    codigo_barras.save(filepath)

    return numero_serie_corto, f"{numero_serie_corto}.png"

if __name__ == "__main__":
    # Ejemplo de uso
    numero_serie_input = input("Introduce el número de serie completo: ")
    generar_codigo_barras(numero_serie_input)
