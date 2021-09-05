# Ejercicio 4.15: Lectura de todos los árboles
# Basándote en la función leer_parque(nombre_archivo, parque) del Ejercicio 3.18, escribí otra leer_arboles(nombre_archivo) 
# que lea el archivo indicado y devuelva una lista de diccionarios con la información de todos los árboles en el archivo. 
# La función debe devolver una lista conteniendo un diccionario por cada árbol con todos los datos.
# Vamos a llamar arboleda a esta lista.

import csv
from pprint import pprint
import matplotlib.pyplot as plt
import os
import numpy as np


def leer_arboles(nombre_archivo):
    arboleda = []

    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        indices = [headers.index(ncolumna) for ncolumna in headers]
        tipos = [float,float,int,int,int,int,int,str,str,str,str,str,str,str,str,float,float]
        # creo el diccionario con las claves y los valores casteados
        arboleda = [{ ncolumna: tipo(row[index]) for ncolumna, index, tipo in zip(headers, indices, tipos)} for row in rows]

    return arboleda


# arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
# print(f'TOTAL ARBOLES: {len(arboleda)}')

#Como son demasiados diccionarios, listo solo los primeros 10 arboles
# for i, arbol in enumerate(arboleda):
#     if i < 10:
#         pprint(arbol)

#===================================================================================================================================
# Ejercicio 4.16: Lista de altos de Jacarandá
# Usando comprensión de listas y la variable arboleda podés por ejemplo armar la lista de la altura de los árboles.
# Usá los filtros (recordá la Sección 4.3) para armar la lista de alturas de los Jacarandás solamente.

def alto_jacaranda():
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    return [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

# print(len(H))

# for altura in H:
#     pprint(altura)

#===================================================================================================================================
# Ejercicio 4.17: Lista de altos y diámetros de Jacarandá
# En el ejercicio anterior usaste una sola linea para seleccionar las alturas de los Jacarandás en parques porteños. 
# Ahora te proponemos que armes una nueva lista que tenga pares (tuplas de longitud 2) conteniendo no solo el alto 
# sino también el diámetro de cada Jacarandá en la lista.

def alto_diametro_jacaranda():
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    return [ (float(arbol['altura_tot']), float(arbol['diametro']) )  for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']


#===================================================================================================================================
# Ejercicio 4.18: Diccionario con medidas
# Te pedimos que armes un diccionario en el que estas especies sean las claves y los valores asociados sean los datos que generaste 
# en el ejercicio anterior. Más aún, organizá tu código dentro de una función medidas_de_especies(especies,arboleda) que recibe 
# una lista de nombres de especies y una lista como la del Ejercicio 4.15 y devuelve un diccionario cuyas claves son estas especies 
# y sus valores asociados sean las medidas generadas en el ejercicio anterior.


# especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']


def medida_de_especies(especies, arboleda):
    dic = { especie: [ (float(arbol['altura_tot']), float(arbol['diametro']) )  for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
    return dic


# diccionario = medida_de_especies(especies, arboleda)

# print(len(diccionario['Eucalipto']))
# print(len(diccionario['Palo borracho rosado']))
# print(len(diccionario['Jacarandá']))
#===================================================================================================================================
# Ejercicio 5.25: Histograma de altos de Jacarandás
# Usando tu trabajo en el Ejercicio 4.16, generá un histograma con las alturas de los Jacarandás en el dataset.

def histograma():
    nombre_archivo = os.path.join('..','Data','arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    plt.hist(altos,bins=50)
    plt.show()

#===================================================================================================================================
# Ejercicio 5.26: Scatterplot (diámetro vs alto) de Jacarandás
# Escribí una función scatter_hd(lista_de_pares) que a partir de una lista de pares como la que generaste en el Ejercicio 4.17 
# genere un scatterplot para visualizar la relación entre altura y diámetro de los Jacarandás del dataset.


def scatter_hd(lista_de_pares):
    arreglo = np.array(lista_de_pares) 
    h = [t[0] for t in arreglo]
    d = [t[1] for t in arreglo]
    colors = np.random.rand(3255)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.scatter(d, h, c=colors, alpha=0.25)
    plt.show()
