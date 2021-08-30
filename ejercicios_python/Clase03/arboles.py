# Ejercicio 3.18: Lectura de los árboles de un parque
# Definí una función leer_parque(nombre_archivo, parque) que abra el archivo indicado y devuelva una lista de diccionarios
#  con la información del parque especificado. La función debe devolver, en una lista un diccionario con todos los datos por
#   cada árbol del parque elegido (recordá que cada fila del csv es un árbol).

import csv
from pprint import pprint
from collections import Counter

def leer_parque(nombre_archivo, parque):
    arboles_parque = []

    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)

        for n_fila, fila in enumerate(filas, start=1):
            #creo tuplas con zip() y luego las transformo en un diccionario
            record = dict(zip(encabezado, fila))
            
            if record['espacio_ve'] == parque:
                arboles_parque.append(record)
            
    
    return arboles_parque



arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')

print(f'\n{"-" * 45}\nEjércicio 3.18\n')
#cantidad de arboles en el parque
print(f'TOTAL ARBOLES EN GRAL. PAZ: {len(arboles)}')

#Como son demasiados diccionarios, listo solo los primeros 10 arboles
# for i, arbol in enumerate(lista, start=1):
#     if i < 11:
#         pprint(arbol)

#=================================================================================================================
# Ejercicio 3.19: Determinar las especies en un parque
# Escribí una función especies(lista_arboles) que tome una lista de árboles como la generada en el ejercicio anterior y 
# devuelva el conjunto de especies (la columna 'nombre_com' del archivo) que figuran en la lista.

def especies(lista_arboles):
    especie = []
    
    for arbol in lista_arboles:
        especie.append(arbol['nombre_com'])
    #conjunto de especies unicas
    unicos = set(especie)

    return unicos


print(f'\n{"-" * 45}\nEjércicio 3.19\n')
print('ESPECIES DE ARBOLES EN GENERAL PAZ:\n')
#listado de las especies
for i in especies(arboles):
    print(i)

#cantidad de especies distintas
# print(len(especies(arboles)))

#=================================================================================================================
# Ejercicio 3.20: Contar ejemplares por especie
# Usando contadores como en el Ejercicio 3.11, escribí una función contar_ejemplares(lista_arboles) que, dada una lista 
# como la que generada con leer_parque(), devuelva un diccionario en el que las especies (recordá, es la columna 'nombre_com' del archivo) 
# sean las claves y tengan como valores asociados la cantidad de ejemplares en esa especie en la lista dada.

def contar_ejemplares(lista_arboles):
    especies = []
    
    for arbol in lista_arboles:
        especies.append(arbol['nombre_com'])
        
    contador = Counter(especies)

    return contador

# muestro los arboles con sus contadores
# pprint(contar_ejemplares(arboles))

# Luego, combiná esta función con leer_parque() y con el método most_common() para informar las cinco especies más frecuentes
#  en cada uno de los siguientes parques:
# 'GENERAL PAZ'
# 'ANDES, LOS'
# 'CENTENARIO'

print(f'\n{"-" * 45}\nEjércicio 3.20')

def arboles_mas_comunes(zona):
    area = leer_parque('../Data/arbolado-en-espacios-verdes.csv', zona)
    mas_comunes = contar_ejemplares(area).most_common(5)
    for arbol, cantidad in mas_comunes:
        print(f'{arbol}: {cantidad}')

print('\nGENERAL PAZ')
arboles_mas_comunes('GENERAL PAZ')

print('\nLOS ANDES')
arboles_mas_comunes('ANDES, LOS')

print('\nCENTENARIO')
arboles_mas_comunes('CENTENARIO')


#=================================================================================================================
# Ejercicio 3.21: Alturas de una especie en una lista
# Escribí una función obtener_alturas(lista_arboles, especie) que, dada una lista de árboles como la anterior y una especie 
# de árbol (un valor de la columna 'nombre_com' del archivo), devuelva una lista con las alturas (columna 'altura_tot') de lo

def obtener_alturas(lista_arboles, especie):
    alturas = []

    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alturas.append(float(arbol['altura_tot']))
    return alturas


# Usala para calcular la altura promedio y altura máxima de los 'Jacarandá' en los tres parques mencionados.

def altura_max(lista_alturas):
    max = 0.0
    for altura in lista_alturas:
        if altura > max:
            max = altura
    return max

def altura_promedio(lista_alturas):
    suma = 0.0
    contador = 0

    for i, altura in enumerate(lista_alturas, start=1):
        suma += altura
        contador = i
    
    return suma/contador


general_paz = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
alturas_GP = obtener_alturas(general_paz, 'Jacarandá')

andes = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
alturas_andes = obtener_alturas(andes, 'Jacarandá')

centenario = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')
alturas_centenario = obtener_alturas(centenario, 'Jacarandá')


print(f'\n{"-" * 45}\nEjércicio 3.21')

print('\nGENERAL PAZ')
print(f'Altura máxima: {altura_max(alturas_GP)}')
print(f'Altura promedio: {altura_promedio(alturas_GP):.2f}')

print('\nLOS ANDES')
print(f'Altura máxima: {altura_max(alturas_andes)}')
print(f'Altura promedio: {altura_promedio(alturas_andes):.2f}')

print('\nCENTENARIO')
print(f'Altura máxima: {altura_max(alturas_centenario)}')
print(f'Altura promedio: {altura_promedio(alturas_centenario):.2f}')
    

#=================================================================================================================
# Ejercicio 3.22: Inclinaciones por especie de una lista
# Escribí una función obtener_inclinaciones(lista_arboles, especie) que, dada una especie de árbol y una lista de árboles como la anterior, 
# devuelva una lista con las inclinaciones (columna 'inclinacio') de los ejemplares de esa especie.



def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(float(arbol['inclinacio']))
    
    return inclinaciones



print(f'\n{"-" * 45}\nEjércicio 3.22\n')
print('Listado de las inclinaciones de la especie \'Falso Guayabo\' de Parque Centenario:\n')

# listado de las inclinaciones de la especie 'Falso Guayabo' de Parque Centenario
for i in obtener_inclinaciones(centenario, 'Falso Guayabo (Guayaba del Brasil)'):
    print(i)

#=================================================================================================================
# Ejercicio 3.23: Especie con el ejemplar más inclinado
# Combinando la función especies() con obtener_inclinaciones() escribí una función especimen_mas_inclinado(lista_arboles) que, 
# dada una lista de árboles devuelva la especie que tiene el ejemplar más inclinado y su inclinación.

def especimen_mas_inclinado(lista_arboles):
    lista_especies = especies(lista_arboles)
    # máxima inclinación
    max_inclinacion = ''
    # ejemplar con la máxima inclinación
    max_ejemplar = ''
    
    for i, especie in enumerate(lista_especies):
        for inclinacion in obtener_inclinaciones(lista_arboles, especie):
            #seteo como inclinacion max al primer ejemplar
            if i == 0:
                max_inclinacion = inclinacion
                max_ejemplar = especie

            if inclinacion > max_inclinacion:
                max_inclinacion = inclinacion
                max_ejemplar = especie
            
            i += 1

    print(f'Especie mas inclinada: {max_ejemplar}\nInclinación: {max_inclinacion}\n')




print(f'\n{"-" * 45}\nEjércicio 3.23\n')

# Especimen mas inclinado de cada uno de los tres parques
print('GENERAL PAZ')
especimen_mas_inclinado(general_paz)

print('LOS ANDES')
especimen_mas_inclinado(andes)

print('CENTENARIO')
especimen_mas_inclinado(centenario)


#=================================================================================================================
# Ejercicio 3.24: Especie más inclinada en promedio
# Volvé a combinar las funciones anteriores para escribir la función especie_promedio_mas_inclinada(lista_arboles) que, 
# dada una lista de árboles devuelva la especie que en promedio tiene la mayor inclinación y el promedio calculado..

def especie_promedio_mas_inclinada(lista_arboles):
    lista_especies = especies(lista_arboles)
    max_promedio = 0.0
    max_ejemplar = ''
    #suma las inclinaciones de una especie
    suma = 0.0
    contador = 0
    #promedio parcial
    promedio = 0.0
    
    for i, especie in enumerate(lista_especies):
        # Sumo las inclinaciones de la especie
        for inclinacion in obtener_inclinaciones(lista_arboles, especie):
            suma += inclinacion
            contador += 1
        # Calculo el promedio de la especie
        promedio = suma/contador
        # Seteo el primer ejemplar como máximo
        if i == 0:
            max_promedio = promedio
            max_ejemplar = especie
        # Evaluo si el promedio puede ser máximo
        elif promedio > max_promedio:
            max_promedio = promedio
            max_ejemplar = especie

        # Reseteo variables para la próxima especie    
        contador = 0
        suma = 0

    print(f'Especie en promedio mas inclinada: {max_ejemplar}\nPromedio de inclinación: {max_promedio:.2f} grados\n')






print(f'\n{"-" * 45}\nEjércicio 3.24\n')
# Muestro la especie en promedio más inclinada de cada uno de los tres parques
print('GENERAL PAZ')
especie_promedio_mas_inclinada(general_paz)

print('LOS ANDES')
especie_promedio_mas_inclinada(andes)

print('CENTENARIO')
especie_promedio_mas_inclinada(centenario)

