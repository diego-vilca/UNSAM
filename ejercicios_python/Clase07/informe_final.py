# Ejercicio 6.11
import csv
import fileparse

# Ejercicio 2.16: Lista de diccionarios
# Tomá la función que escribiste en el ejercicio anterior y modificala para representar cada cajón del camión 
# con un diccionario en vez de una tupla. En este diccionario usá los campos "nombre", "cajones" y "precio" para 
# representar las diferentes columnas del archivo de entrada.

def leer_camion(nombre_archivo):
    with open(nombre_archivo, encoding='utf8') as f:
        camion = fileparse.parse_csv(f, select=['nombre', 'cajones', 'precio'], types=[str, int, float])
    return camion
    

#=================================================================================================================

# Ejercicio 2.17: Diccionarios como contenedores
# Escribí una función leer_precios(nombre_archivo) que a partir de un conjunto de precios como éste arme un diccionario 
# donde las claves sean los nombres de frutas y verduras, y los valores sean los precios por cajón.

def leer_precios(nombre_archivo):
    with open(nombre_archivo, encoding='utf8') as f:
        precios = fileparse.parse_csv(f, types=[str,float], has_headers=False)
    return precios
    

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

    # for i in camion:
    #     # me fijo si la lista precios es un diccionario (como lo era originalmente)
    #     if isinstance(precios, dict):
    #         lista.append((i['nombre'], i['cajones'], i['precio'], precios[i['nombre']]-i['precio']))
    #     else:
    #         for j in precios:
    #             # si es lista de tuplas, las desempaco
    #             fruta, precio = j
    #             if fruta == i['nombre']:
    #                 lista.append((i['nombre'], i['cajones'], i['precio'], precio - i['precio']))
    if not isinstance(precios, dict):
        precios = dict(precios)
    for i in camion:
        lista.append((i['nombre'], i['cajones'], i['precio'], precios[i['nombre']]-i['precio']))

    return lista


    
#=================================================================================================================
# Ejercicio 6.4: Estructurar un programa como una colección de funciones
# Creá una función imprimir_informe(informe) que imprima el informe.
# Cambiá la última parte del programa de modo que consista sólo en una serie de llamados a funciones, sin ningún cómputo.

def imprimir_funciones(informe):
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
    


# imprimir_funciones(hacer_informe(leer_camion('../Data/camion.csv'), leer_precios('../Data/precios.csv')))

#=================================================================================================================
# Ejercicio 6.5: Crear una función de alto nivel para la ejecución del programa.
# Juntá la última parte de tu programa en una única función informe_camion(nombre_archivo_camion, nombre_archivo_precios).

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    imprimir_funciones(hacer_informe(leer_camion(nombre_archivo_camion), leer_precios(nombre_archivo_precios)))


# informe_camion('../Data/camion.csv', '../Data/precios.csv')

#=================================================================================================================
# Ejercicio 7.4: Función principal
# Usando estas ideas, agregá a tu programa informe_final.py una función f_principal() que tome una lista de parámetros 
# en la línea de comandos y produzca la misma salida que antes.

def f_principal(argv):
    if len(argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    camion = argv[1]
    precios = argv[2]
    informe_camion(camion, precios)


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
