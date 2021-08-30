# Ejercicio 2.8: Administración de errores
# Modificá el programa costo_camion.py para que atrape la excepción con un bloque try - except, 
# imprima un mensaje de aviso (warning) y continúe procesando el resto del archivo.


def costo_camion(nombre_archivo):
    total = 0.0

    f = open(nombre_archivo, 'rt', encoding = 'utf8')
    headers = next(f).split(',')#paso de largo los encabezados

    for line in f:
        fila = line.split(',')

        try:
            total = total + (int(fila[1]) * float(fila[2]))
        except ValueError:
            print('Warning. Faltan datos ')

    f.close()
    return total


costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)







