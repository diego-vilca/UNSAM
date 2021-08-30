# Ejercicio 2.9: Funciones de la biblioteca
# Modificá tu programa costo_camion.py para que use el módulo csv para leer los archivos CSV y probalo en un par de los ejemplos anteriores.
import csv


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



costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)