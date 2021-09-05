# Ejercicio 5.9: Empezando a plotear
# Escribí una función plotear_temperaturas() en un archivo plotear_temperaturas.py que lea el archivo de datos temperaturas.npy 
# (debería tener las 999 mediciones simuladas que creaste recién) y haga un histograma de las temperaturas simuladas.

import matplotlib.pyplot as plt
import numpy as np

def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.hist(temperaturas,bins=12)
    plt.show() 
