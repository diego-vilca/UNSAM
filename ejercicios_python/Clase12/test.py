# Ejercicio 12.4: experimento con 3 métodos

import numpy as np
import matplotlib.pyplot as plt

def generar_listas(N):
    randoms = np.random.randint (1,1000,N)    
    return randoms.tolist()

#====================================================================
# Ordenamiento por selección

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    # comparaciones
    comps = 0
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p, c = buscar_max(lista, 0, n)
        
        #guardo las comparaciones
        comps += c

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1
    
    return comps

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a

    for i in range(a + 1, b + 1):
        # comps += 1
        if lista[i] > lista[pos_max]:
            pos_max = i

    #comparaciones
    comps = b-a

    return pos_max, comps



#====================================================================
# Ordenamiento por inserción

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # comparaciones
    comps = 0

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        
        if lista[i + 1] < lista[i]:
            comps += reubicar(lista, i + 1)
        else:
            comps += 1
        # print("DEBUG: ", lista)

    return comps

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]
    #comparaciones
    comps = 0

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p

    comps += 1
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        comps += 1

    lista[j] = v

    return comps




#====================================================================
# Ordenamiento por burbujeo


def ord_burbujeo(lista):
    """Ordena una lista de elementos según el método de burbujeo.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    lenLista = len(lista)
    #comparaciones
    comps = 0


    #recorro los elementos de la lista
    for i in range(lenLista):

        #Como el ultimo j de cada iteracion i queda ordenado fijo al final, en cada vuelta de i ordeno 
        #los valores de la lista sin tener en cuenta el ultimo valor.
        for j in range((lenLista-i)-1):  
            comps += 1
            #comparo dos elementos contiguos de la lista
            #si el orden es el adecuado los deja como están, si no, los intercambio.
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return comps


def experimento(N, k):
    '''A partir de un largo de lista (N) y cierta cantidad de iteraciones (k) devuelve el promedio de las comparaciones
    de los algoritmos de ordenamiento.
    pre: N, k enteros positivos
    post: regresa una tupla con los promedios de cada comparacion
    '''
    comps_burb = 0.0
    comps_ins = 0.0
    comps_sel = 0.0

    for _ in range(k):
        lista = generar_listas(N)

        comps_burb += ord_burbujeo(lista.copy())
        # print(lista)
        comps_ins += ord_insercion(lista.copy())
        # print(lista)
        comps_sel += ord_seleccion(lista.copy())
        # print(lista)

    return comps_burb/k, comps_ins/k, comps_sel/k
    

def experimento_vectores(Nmax):
    largoLista = np.arange(Nmax) + 1

    #creo los vectores donde guardare las comparaciones
    comparaciones_seleccion = np.zeros(Nmax)
    comparaciones_insercion = np.zeros(Nmax)
    comparaciones_burbujeo = np.zeros(Nmax)

    for i, n in enumerate(largoLista):
        #genero la lista
        lista = generar_listas(n)
        # print(lista)
        comparaciones_seleccion[i] = ord_seleccion(lista.copy())
        comparaciones_insercion[i] = ord_insercion(lista.copy())
        comparaciones_burbujeo[i] = ord_burbujeo(lista.copy())
        # print(comparaciones_seleccion)
        # print(comparaciones_insercion)
        # print(comparaciones_burbujeo)

    # # ahora grafico largos de listas contra las comparaciones realizadas por cada método de ordenamiento.
    # plt.plot(largoLista, comparaciones_seleccion, label = 'Ord. Secuencial')
    # plt.plot(largoLista, comparaciones_insercion, label = 'Ord. Inserción')
    # plt.plot(largoLista, comparaciones_burbujeo, label = 'Ord. Burbujeo')
    # # limit y
    # plt.ylim(0, Nmax)
    # # limit x
    # plt.xlim(0, 150)
    # plt.xlabel("Largo de la lista")
    # plt.ylabel("Cantidad de comparaciones")
    # plt.title("Complejidad de la Búsqueda")
    # plt.legend()
    # plt.show()


# def f_principal():
#     print(experimento(10, 100))

# if __name__ == '__main__':
#     f_principal()
    