import csv

# Ejercicio 2.16: Lista de diccionarios
# Tomá la función que escribiste en el ejercicio anterior y modificala para representar cada cajón del camión 
# con un diccionario en vez de una tupla. En este diccionario usá los campos "nombre", "cajones" y "precio" para 
# representar las diferentes columnas del archivo de entrada.

def leer_camion(nombre_archivo):
    camion = []
    

    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        # camion.append(next(rows))

        for n_fila, fila in enumerate(filas, start = 1):
            #creo tuplas con zip() y luego las transformo en un diccionario
            record = dict(zip(encabezados, fila))
            d = {}

            d['nombre'] = record['nombre']
            d['cajones'] = int(record['cajones'])
            d['precio'] = float(record['precio'])

            camion.append(d)

    
    return camion

#=================================================================================================================

# Ejercicio 2.17: Diccionarios como contenedores
# Escribí una función leer_precios(nombre_archivo) que a partir de un conjunto de precios como éste arme un diccionario 
# donde las claves sean los nombres de frutas y verduras, y los valores sean los precios por cajón.

def leer_precios(nombre_archivo):
    d = {}

    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        
        try:
            for n_fila, fila in enumerate(rows, start=1):
                d[fila[0]] = float(fila[1])
                
        except IndexError:
            print(f'Fila {n_fila} de {nombre_archivo} : No pude interpretar: {fila}\n')
    
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
    compra = leer_camion('../Data/fecha_camion.csv')
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

    # print(f'Total costos: ${total_compras}')
    # print(f'Total ventas: ${total_ventas}')
    print(f'Balance: ${balance:0.2f}')


# balance()

#=================================================================================================================

# EJERCICIO 3.16

def hacer_informe(camion, precios):
    lista = []

    for i in camion:
        lista.append((i['nombre'], i['cajones'], i['precio'], precios[i['nombre']]-i['precio']))

    return lista



camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
head_formateado = ''
separador = ''


#creo el encabezado y el separador
for encabezado in headers:
    head_formateado += f'{encabezado:>10} '
    separador += f'{"-" * 10} '

#imprimo encabezado y separador
print(head_formateado)
print(separador)

#imprimo lista formateada
for nombre, cajones, precio, cambio in informe:
    #agrego el simbolo dolar y remuevo ceros insignificantes con 'g'
    formato_precio = f'${precio:g}'
    print(f'{nombre:>10s} {cajones:>10d} {formato_precio:>10} {cambio:>10.2f}')
   
    
#=================================================================================================================