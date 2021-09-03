# Ejercicio 5.2: Generala no necesariamente servida
# Escribí una función llamada prob_generala(N) que, a partir de un parámetro N y usando las funciones del Ejercicio 5.1 
# realice una simulación con N repeticiones, para estimar la probabilidad de obtener una generala al finalizar una mano de tres tiradas. 
# La función debe devolver un número entre 0 y 1. Guardala en un archivo generala.py para el cierre de la clase.


import random
from collections import Counter
from pprint import pprint


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
        print(f'tirada 1: {tirada_1}')

        if not es_generala(tirada_1):# tengo que realizar una segunda tirada
            # obtengo las ocurrencias de cada número de la tirada
            tirada_1 = Counter(tirada_1)
            # número con mas ocurrencias de la tirada 1. Si todos los numeros de la tirada son distintos, o si 2 numeros se repiten 2 veces, tomo el primero
            num_a_buscar = max(tirada_1, key = tirada_1.get)
            # cantidad de veces que aparece el número de la tirada 1 con mas repeticiones
            repetido_tirada_1 = tirada_1[num_a_buscar] 
            print(f'numero: {num_a_buscar}')
            print(f'cant repes 1: {repetido_tirada_1}')

            # realizo una segunda tirada
            tirada_2 = [random.randint(1,6) for _ in range(5 - repetido_tirada_1)]
            print(f'tirada 2: {tirada_2}')

            # pregunto si con la segunda tirada hice generala
            # comparo que en la segunda tirada los numeros sean iguales y si coinciden con los que conservo de la tirada 1, sumo una generala
            if es_generala(tirada_2) and max(tirada_2) == num_a_buscar:
                G += 1

            else: # no hubo generala en la segunda tirada, tiro un tercera vez
                tirada_2 = Counter(tirada_2)

                # si esta num_a_buscar en la tirada_2 lo conservo y tiro los demas
                if num_a_buscar in tirada_2:
                    # me fijo cuantas veces salio num_a_buscar en la segunda tirada
                    repetido_tirada_2 = tirada_2[num_a_buscar]
                    print(f'cant repes 2: {repetido_tirada_2}')

                    # realizo la tercer tirada
                    tirada_3 = [random.randint(1,6) for _ in range(5 - (repetido_tirada_2 + repetido_tirada_1))]
                    print(f'tirada 3: {tirada_3}')
                # no esta num_a_buscar, entonces vuelvo a tirar todos
                else:
                    tirada_3 = [random.randint(1,6) for _ in range(5 - repetido_tirada_1)]
                    print(f'tirada 3: {tirada_3}')

                # si en la tercer tirada todos los numeros son distintos y coinciden con el valor que estoy buscando, hice generala
                if es_generala(tirada_3) and max(tirada_3) == num_a_buscar:
                    G += 1
                


        # realice generala en una tirada
        else:
            G += 1

    prob = G / N
    print(f'cant generalas: {G}')
    print(f'probabilidad: {prob}')