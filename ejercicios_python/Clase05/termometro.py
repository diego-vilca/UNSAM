# Ejercicio 5.8: Guardar temperaturas
# Ampliá el código de la función medir_temp(n) en tu archivo termometro.py que escribiste en el Ejercicio 5.6 para que además 
# de devolver las temperaturas simuladas, guarde el vector con estas temperaturas en el directorio Data de tu carpeta de ejercicios, 
# en un archivo llamado temperaturas.npy. Hacé que corra n = 999 veces.

import numpy as np
import random

def medir_temp(n):
    
    temp_real = 37.5
    mu = 0
    sigma = 0.2

    temps = [ temp_real + random.normalvariate(mu, sigma) for _ in range(n)]

    # guardo las temperaturas
    np.save('../Data/temperaturas.npy', temps)

    return temps


def resumen_temp(n):
    temperaturas = medir_temp(n)

    maximo = max(temperaturas)
    minimo = min(temperaturas)
    promedio = sum(temperaturas)/n
    # ordeno la lista y calculo la mediana
    lista_ord = sorted(temperaturas)

    if len(lista_ord) % 2 != 0:
        i = len(lista_ord) // 2
        mediana = lista_ord[i]
    else:
        i = int(len(lista_ord) / 2)
        mediana = (lista_ord[i] + lista_ord[i-1]) / 2
    
    
    return (maximo, minimo, promedio, mediana)


