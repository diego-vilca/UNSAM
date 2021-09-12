# Ejercicio 6.15: Insertar un elemento en una lista

def donde_insertar(lista, x):
    '''Recibe una lista ordenada y devuelve la posicion del elemento
    en la lista, o la posicion donde se podria insertar el elemento para
    que la lista permanezca ordenada (si no esta en la lista)
    '''
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    mitad = 0
    encontrado = False
    # print(f'[DEBUG] izq |der |medio')

    while izq <= der:
        medio = (izq + der) // 2
        #comentar el print
        # print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')

        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            encontrado = True
        else:
            mitad = medio  # voy guardando el indice medio en la variable mitad

        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

    #si el valor no se encuentra en la lista...
    if not encontrado:
        try:
            if lista[mitad] > x:
                pos = mitad
                # print('medio')
            elif lista[mitad] < x:
                # print('medio + 1')
                pos = mitad + 1
        except IndexError:
            print('Por favor, ingrese una lista no vacia')


    return pos

#=================================================================================

def insertar(lista, x):
    indice = donde_insertar(lista, x)

    # si el elemento no se encuentra en la lista, lo agrego 
    if x not in lista:
        if indice == len(lista):
            lista.append(x)
        else:
            lista.insert(indice, x)

    return indice

