# Ejercicio 2.10: Ejecución desde la línea de comandos con parámetros
# Copiá el contenido de costo_camion.py a un nuevo archivo llamado camion_commandline.py que 
# incorpore la lectura de parámetros por línea de comando

import csv
import sys

def costo_camion(nombre_archivo):
    total = 0.0

    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
        try:
            total = total + (int(row[1]) * float(row[2]))
        except ValueError:
            print('Cuidado, dato no válido')

    f.close()
    return total


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'


costo = costo_camion(nombre_archivo)
print('Costo total:', costo)