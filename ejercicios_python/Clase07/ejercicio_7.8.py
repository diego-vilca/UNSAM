# Ejercicio 7.8: Sumas
# En este ejercicio vas a realizar dos implementaciones correspondientes a la función sumar_enteros definida recién.

# En la primera implementación te pedimos que uses un ciclo.
# En la segunda te pedimos que lo hagas sin ciclos: implementá la función de manera que trabaje en tiempo constante 
# (es decir, usando una cantidad de operaciones que no depende de las entradas a la función.

# Un invariante de ciclo es una aseveración que debe ser verdadera al comienzo de cada iteración del ciclo y al salir del mismo.

def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0 # invariante
    if hasta > desde:
        for i in range(desde, hasta + 1):
            suma += i

    return suma



def sumar_enteros_2(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0
    if hasta > desde:
        # número triangular desde-1
        a = ((desde - 1) * desde)/2
        # número triangular hasta
        b = (hasta * (hasta + 1))/2
        #diferencia de números triangulares
        suma = b - a

    return int(suma)

