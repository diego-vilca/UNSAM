# import csv
import informe_funciones

def costo_camion(nombre_archivo):
    total = 0.0
    camion = informe_funciones.leer_camion(nombre_archivo)

    for fruta in camion:
        total += fruta['cajones'] * fruta['precio']

    return total


    

# costo = costo_camion('../Data/missing.csv')
# costo = costo_camion('../Data/fecha_camion.csv')
# print('Costo total:', costo)