#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
# Comentarios: El error es de semántica y se da porque la función solo evalúa el primer cáracter de la cadena , cuando se supone que debe recorrerla 
# toda buscando la vocal. También, como la función se llama 'tiene_a()' agrego una condición al 'if' que tenga en cuenta las vocales mayúsculas.
# Corrección: Saco el 'return False' fuera del while

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True            
        i += 1

    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
# Comentario: El error era de sintaxis, faltaban los dos puntos al final de la declaración de la funcion y de las 
# instrucciones while e if. Comparaba erronemente con el operador '='  y la palabra 'False' estaba mal escrita
# Correccion: Puse los ':' al final del def, while e if. Corregi '=' por '==' y 'Falso' por 'False'.
# La funcion no contemplaba el caso de prueba en mayúsculas asi que agregue la condición correspondiente.

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')


#%%
#Ejercicio 3.3. Función tiene_uno()
# Comentarios: El error se da en tiempo de ejecución, en el tercer caso de prueba. 
# La función 'tiene_uno' necesita que su argumento sea una cadena para poder utilizar la función len() pero en cambio se le pasa un entero.
# Corrección: convierto el entero en cadena agregandole comillas.

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno('1984')

#%%
#Ejercicio 3.4. Función suma()
# Comentario: El error es de semántica y se da porque se asigna a una variable una función que no devuelve nada.
# Corrección: Hago que la función devuelva un resultado agregandole 'return'

def suma(a,b):
    c = a + b
    return c


a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.5. Función leer_camion()
# Comentarios: Es un error semántico, al definir 'registro' fuera del bucle lo que hago en cada iteración del for es sobreescribir sus
# referencias guardadas en la lista.
# Corrección: Definir 'registro' dentro del bucle.

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)




# %%
