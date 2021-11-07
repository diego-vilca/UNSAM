# Ejercicio 12.2: burbujeo
# Programá una función ord_burbujeo(lista) que implemente este método de ordenamiento. 
# Debe tomar una lista y devolver la lista ordenada. ¿Cuántas comparaciones realiza esta función en una lista de largo n?


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


    # En mi primer for tengo mi lista de longitud n, y en el segundo for durante la primer vuelta, tengo una lista de longitud n-1.
    # Osea que en esa primer vuelta la complejidad del algorítmo seria n*(n-1) y si desestimo la constante (considerando n muy grande) me quedaria de n^2.
    # Eso seria en el peor de los casos, ya que a partir de la segunda vuelta del segundo for, la lista que comparo se hace mas pequeña por cada iteración.