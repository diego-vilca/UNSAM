# ticker.py

from vigilante import vigilar
from formato_tabla import crear_formateador
from informe_final import leer_camion
import csv

def ticker(camion_file, log_file, fmt):
    camion = leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file))
    # filtro los datos
    rows = (fila for fila in rows if fila['nombre'] in camion)
    # formateo la salida
    formateador = crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    
    for row in rows:
        registro = (str(elemento) for elemento in row.values())
        formateador.fila(registro)


def parsear_datos(lines):
    rows = csv.reader(lines)
    # Elijo columnas
    rows = ((row[index] for index in [0, 1, 2]) for row in rows)
    # Cambio tipos de datos
    rows = ((func(val) for func, val in zip([str, float, int], row)) for row in rows)
    # Creo el diccionario
    rows = (dict(zip(['nombre', 'precio', 'volumen'], row)) for row in rows)
    return rows

# correr sim_mercado.py
# if __name__ == '__main__':
#     ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'txt')
