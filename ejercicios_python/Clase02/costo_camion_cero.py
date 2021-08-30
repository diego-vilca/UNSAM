# Ejercicio 2.2: Lectura de un archivo de datos
# Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad de cajones cargados en el camión, 
# y un precio de compra por cada cajón de ese grupo. Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas, 
# y calcule el precio pagado por los cajones cargados en el camión.

# total = 0.0

# f = open('../Data/camion.csv', 'rt', encoding = 'utf8')
# headers = next(f).split(',')

# for line in f:
#     fila = line.split(',')
#     total = total + (int(fila[1]) * float(fila[2]))

# f.close()

# print('Costo total:', total)

#============================================================================================
# Ejercicio 2.6: Transformar un script en una función
# Transformá el programa costo_camion.py (que escribiste en el Ejercicio 2.2 de la sección anterior) en una función costo_camion(nombre_archivo). 
# Esta función recibe un nombre de archivo como entrada, lee la información sobre los cajones que cargó el camión y devuelve 
# el costo de la carga de frutas como una variable de punto flotante.

def costo_camion(nombre_archivo):
    total = 0.0

    f = open(nombre_archivo, 'rt', encoding = 'utf8')
    headers = next(f).split(',')#paso de largo los encabezados

    for line in f:
        fila = line.split(',')
        total = total + (int(fila[1]) * float(fila[2]))

    f.close()
    return total



costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)