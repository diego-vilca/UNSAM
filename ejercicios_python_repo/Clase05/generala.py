# Ejercicio 5.2: Generala no necesariamente servida
# Escribí una función llamada prob_generala(N) que, a partir de un parámetro N y usando las funciones del Ejercicio 5.1 
# realice una simulación con N repeticiones, para estimar la probabilidad de obtener una generala al finalizar una mano de tres tiradas. 
# La función debe devolver un número entre 0 y 1. Guardala en un archivo generala.py para el cierre de la clase.


import random
from collections import Counter
# from pprint import pprint


def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    # print(tirada)
    return tirada


def es_generala(tirada):
    for i in range(len(tirada)):
        if tirada[i] != tirada[0]:
            return False
    return True







def prob_generala(N):
    G = 0
    prob = 0.0

    # realizo la iteracion x N
    for i in range(N):
        # realizo la primer tirada
        tirada_1 = tirar()

        # si no hay generala, tengo que realizar una segunda tirada
        if not es_generala(tirada_1):
            # obtengo las ocurrencias de cada número de la primer tirada
            tirada_1 = Counter(tirada_1)
            # número con mas ocurrencias de la tirada 1. Si todos los numeros de la tirada son distintos, o si 2 numeros se repiten 2 veces, tomo el primero
            num_a_buscar = max(tirada_1, key = tirada_1.get)
            # cantidad de veces que aparece el número con mas repeticiones de la tirada 1
            cant_apariciones_1 = tirada_1[num_a_buscar] 

            # realizo una segunda tirada
            tirada_2 = [random.randint(1,6) for _ in range(5 - cant_apariciones_1)]
            

            # pregunto si con la segunda tirada hice generala
            if es_generala(tirada_2) and max(tirada_2) == num_a_buscar:
                # incremento el número de generalas
                G += 1

            # si no hubo generala en la segunda tirada...
            else: 
                tirada_2 = Counter(tirada_2)
                # número que mas aparecio en la segunda tirada
                num_2 = max(tirada_2, key = tirada_2.get)
                # cantidad de veces que aparecio ese número
                cant_apariciones_2 = tirada_2[num_2]

                # si en la tirada 2 existe un número que aparece mas veces que el número buscado de la primer tirada, lo reemplazo
                if cant_apariciones_2 > cant_apariciones_1:
                    # ahora busco el número con mas apariciones de la tirada 2
                    num_a_buscar = num_2

                    # realizo la tercer tirada
                    tirada_3 = [random.randint(1,6) for _ in range(5 - cant_apariciones_2)]

                    # si en la tercer tirada todos los numeros son distintos y coinciden con el valor que estoy buscando, hice generala
                    if es_generala(tirada_3) and max(tirada_3) == num_a_buscar:
                        # incremento el número de generalas
                        G += 1

                # sino, sigo buscando el número con mas apariciones de la primer tirada
                else:

                    # si el número buscado de la primer tirada aparece en la segunda, tiro los que restan
                    if num_a_buscar in tirada_2:
                        # me fijo cuantas veces se repitio el num_a_buscar de la primer tirada, en la segunda
                        cant_repeticiones_1 = tirada_2[num_a_buscar]

                        # realizo la tercer tirada
                        tirada_3 = [random.randint(1,6) for _ in range(5 - (cant_apariciones_1 + cant_repeticiones_1))]

                    # si el número buscado de la primer tirada no aparece en la segunda, tiro todos
                    else:
                        tirada_3 = [random.randint(1,6) for _ in range(5 - cant_apariciones_1)]

                    # si en la tercer tirada todos los numeros son distintos y coinciden con el valor que estoy buscando, hice generala
                    if es_generala(tirada_3) and max(tirada_3) == num_a_buscar:
                        G += 1

        # realice generala en la primer tirada
        else:
            G += 1
        


    prob = G/N
    # print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    # print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

    return prob
    