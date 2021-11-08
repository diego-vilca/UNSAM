# Ejercicio 12.8

import numpy as np
import matplotlib.pyplot as plt
import timeit as tt

#========================================================================
# Ordenamiento de selección


def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]

        # reducir el segmento en 1
        n = n - 1
    
    return lista

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max


#========================================================================
# Ordenamiento de inserción

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
    return lista

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v



#========================================================================
# Ordenamiento por burbujeo

def ord_burbujeo(lista):
    """Ordena una lista de elementos según el método de burbujeo.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    lenLista = len(lista)

    #recorro los elementos de la lista
    for i in range(lenLista):
        # print("i = ", i)

        #Como el ultimo j de cada iteracion i queda ordenado fijo al final, en cada vuelta de i ordeno 
        #los valores de la lista sin tener en cuenta el ultimo valor.
        for j in range((lenLista-i)-1):  
            # print("\tj = ", j)

            #comparo dos elementos contiguos de la lista
            #si el orden es el adecuado los deja como están, si no, los intercambio.
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

#========================================================================
# Ordenamiento merge

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado

#========================================================================
def generar_lista(N):
    '''genera una lista de N elementos de valores aleatorios entre 1 y 1000.
    pre: N > 0
    post: devuelve una lista de N elementos de valores aleatorios
    '''
    randoms = np.random.randint (1,1000,N)    
    return randoms.tolist()

def generar_listas(Nmax):
    '''genera una lista de listas, una de cada longitud entre 1 y Nmax.
    pre: Nmax > 0
    post: devuelve una lista de listas
    '''
    listas = []
    for N in range(1, Nmax + 1):
        listas.append(generar_lista(N))
    # print(listas)
    return listas


def experimento_timeit(Nmax):
    '''Calcula el tiempo de ejecución realizadas por cada método de ordenamiento
    para listas de longitud entre 1 a Nmax, y grafica los resultados.
    pre: Nmax entero positivo
    post: grafica el tiempo de ejecución por cada método de ordenamiento
    '''
        
    tiempo_seleccion = np.zeros(Nmax)
    tiempo_insercion = np.zeros(Nmax)
    tiempo_burbujeo = np.zeros(Nmax)
    tiempo_merge = np.zeros(Nmax)

    listas = generar_listas(Nmax)
    global lista

    for i, lista in enumerate(listas):

        tiempo_seleccion[i] = tt.timeit('ord_seleccion(lista.copy())', number = 10, globals = globals())
        tiempo_insercion[i] = tt.timeit('ord_insercion(lista.copy())', number = 10, globals = globals())
        tiempo_burbujeo[i] = tt.timeit('ord_burbujeo(lista.copy())', number = 10, globals = globals())
        tiempo_merge[i] = tt.timeit('merge_sort(lista.copy())', number = 10, globals = globals())

    # ahora grafico largos de listas contra los tiempos de ejecución por cada método de ordenamiento.
    plt.plot(tiempo_seleccion, c = 'blue', label = 'Ord. Secuencial')
    plt.plot(tiempo_insercion, c='green', label = 'Ord. Inserción')
    plt.plot(tiempo_burbujeo, c='red', label = 'Ord. Burbujeo')
    plt.plot(tiempo_merge, c='orange', label = 'Merge Sort')
    plt.ylabel("Tiempo de ejecución")
    plt.xlabel("Longitud de lista")
    plt.title("Tiempo de ejecución de cada método")
    plt.legend()
    plt.show()