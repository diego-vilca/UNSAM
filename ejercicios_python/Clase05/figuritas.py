import random
import numpy as np

# 5.10
def crear_album(figus_total):
    album = np.zeros(figus_total)
    return album

# 5.11
def album_incompleto(A):
    if 0 in A:
        return True
    return False

# 5.12
def comprar_figu(figus_total):
    figu = random.randint(1, figus_total)
    return figu

# 5.13
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    contador_figus = 0
    while album_incompleto(album):
        figurita = comprar_figu(figus_total)
        contador_figus += 1
        if album[figurita-1] == 0:
            album[figurita-1] = 1
        else:
            album[figurita-1] += 1
        # print(album)
    return contador_figus

# 5.14
def promedio():
    n_repeticiones = 1000
    figus_total = 6
    promedio_figus = np.mean([ cuantas_figus(figus_total) for _ in range(n_repeticiones)])
    return promedio_figus

# 5.15
def experimento_figus(n_repeticiones, figus_total):
    return np.mean([ cuantas_figus(figus_total) for _ in range(n_repeticiones)])
    
