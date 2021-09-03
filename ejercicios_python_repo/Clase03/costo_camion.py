# Ejercicio 3.8: Un ejemplo práctico de enumerate()
# Recordá que el archivo Data/missing.csv contiene datos sobre los cajones de un camión, pero tiene algunas filas que faltan. 
# Usando enumerate(), modificá tu programa costo_camion.py de forma que imprima un aviso (warning) cada vez que encuentre una fila incorrecta.

import csv


def costo_camion(nombre_archivo):
    total = 0.0

    f = open(nombre_archivo)
    filas = csv.reader(f)
    headers = next(filas)

    for n_fila, fila in enumerate(filas, start = 1):
        try:
            total = total + (int(fila[1]) * float(fila[2]))
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')

    f.close()
    return total



costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)