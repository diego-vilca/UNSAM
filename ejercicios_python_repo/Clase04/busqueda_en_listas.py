# Ejercicio 4.3: Búsquedas de un elemento
# Busca el último elemento
def buscar_u_elemento(lista, e):
    ultima_posicion = -1
    
    for i, elemento in enumerate(lista):
        if elemento == e:
            ultima_posicion = i

    return ultima_posicion


# Busca total de ocurrencias de un elemento
def buscar_n_elemento(lista, e):
    cantidad = 0
    for elemento in lista:
        if elemento == e:
            cantidad += 1
    return cantidad

#===============================================================================================

# Ejercicio 4.4: Búsqueda de máximo y mínimo

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    
    for i, e in enumerate(lista): # Recorro la lista y voy guardando el mayor
        if i == 0:
            m = e
        else:
            if e > m:
                m = e
    return m




def minimo(lista):
    '''Devuelve el mínimo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el mínimo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    
    for i, e in enumerate(lista): # Recorro la lista y voy guardando el menor
        if i == 0:
            m = e
        else:
            if e < m:
                m = e
    return m


