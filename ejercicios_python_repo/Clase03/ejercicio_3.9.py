# Esta transformación es un truco sumamente útil cuando tenés que procesar muchos archivos de datos. 
# Por ejemplo, suponé que querés hacer que el programa costo_camion.py trabaje con diferentes archivos de entrada, 
# pero que no le importe la posición exacta de la columna que tiene la cantidad de cajones o el precio. 
# Es decir, que entienda que la columna tiene el precio por su encabezado y no por su posición dentro del archivo.

import csv


def costo_camion(nombre_archivo):
    total = 0.0

    f = open(nombre_archivo)
    filas = csv.reader(f)
    encabezados = next(filas)

    for n_fila, fila in enumerate(filas, start = 1):
        #creo tuplas con zip() y luego las transformo en un diccionario
        record = dict(zip(encabezados, fila))
        try:
            total = total + (int(record['cajones']) * float(record['precio']))
        
        # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')

    f.close()
    return total



# costo = costo_camion('../Data/missing.csv')
costo = costo_camion('../Data/fecha_camion.csv')
print('Costo total:', costo)