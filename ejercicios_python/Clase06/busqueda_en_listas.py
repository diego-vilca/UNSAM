def busqueda_lineal_lordenada(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    # l_ordenada = sorted(lista)
    pos = -1  # comenzamos suponiendo que e no está
    # for i, z in enumerate(l_ordenada): # recorremos la lista
    for i, z in enumerate(lista): 
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        if z > e:
            break
    return pos