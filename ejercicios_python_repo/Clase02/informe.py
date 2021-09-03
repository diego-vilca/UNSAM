import csv

# Ejercicio 2.15: Lista de tuplas
# En este archivo, definí una función leer_camion(nombre_archivo) que abre un archivo con el contenido de un camión, 
# lo lee y devuelve la información como una lista de tuplas.

# def leer_camion(nombre_archivo):
#     camion = []

#     with open(nombre_archivo, 'rt') as f:
#         rows = csv.reader(f)
#         next(rows)
#         # camion.append(next(rows))

#         for row in rows:
#             lote = (row[0], int(row[1]), float(row[2]))
#             camion.append(lote)
#     return camion

    
# lista = (leer_camion('../Data/camion.csv'))

# for linea in lista:
#     print(linea)

#=================================================================================================================

# Ejercicio 2.16: Lista de diccionarios
# Tomá la función que escribiste en el ejercicio anterior y modificala para representar cada cajón del camión 
# con un diccionario en vez de una tupla. En este diccionario usá los campos "nombre", "cajones" y "precio" para 
# representar las diferentes columnas del archivo de entrada.

def leer_camion(nombre_archivo):
    camion = []
    

    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        next(rows)
        # camion.append(next(rows))

        for row in rows:
            d = {}

            d['nombre'] = row[0]
            d['cajones'] = int(row[1])
            d['precio'] = float(row[2])

            camion.append(d)

    
    return (camion)

#=================================================================================================================

# Ejercicio 2.17: Diccionarios como contenedores
# Escribí una función leer_precios(nombre_archivo) que a partir de un conjunto de precios como éste arme un diccionario 
# donde las claves sean los nombres de frutas y verduras, y los valores sean los precios por cajón.

def leer_precios(nombre_archivo):
    d = {}

    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        
        try:
            for row in rows:
                d[row[0]] = float(row[1])
        except IndexError:
            print('Cuidado, se encontro una linea con datos faltantes')
    
    return d

#=================================================================================================================

# Ejercicio 2.18: Balances
# Supongamos que los precios en camion.csv son los precios pagados al productor de frutas mientras que los precios 
# en precios.csv son los precios de venta en el lugar de descarga del camión.

# Ahora vamos calcular el balance del negocio: juntá todo el trabajo que hiciste recién en tu programa informe.py 
# (usando las funciones leer_camion() y leer_precios()) y completá el programa para que con los precios del camión 
# (Ejercicio 2.16) y los de venta en el negocio (Ejercicio 2.17) calcule lo que costó el camión, lo que se recaudó 
# con la venta, y la diferencia. ¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.

def balance():
    compra = leer_camion('../Data/camion.csv')
    precio_venta = leer_precios('../Data/precios.csv')
    total_compras = 0.0
    total_ventas = 0.0

    #calculo lo que gasto en comprar la mercaderia
    for s in compra:
        #calculo cuanto gaste
        total_compras += s['cajones'] * s['precio']

    #calculo lo que se vendio
    for t in compra:
        total_ventas +=  t['cajones'] * precio_venta[t['nombre']]
        
            
    balance = total_ventas - total_compras

    print(f'Total costos: ${total_compras}')
    print(f'Total ventas: ${total_ventas}')
    print(f'Balance: ${balance:0.2f}')
    
