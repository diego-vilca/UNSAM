# Ejercicio 11.14: precio_alquiler ~ superficie
import numpy as np
import matplotlib.pyplot as plt


def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b


superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

a, b = ajuste_lineal_simple(superficie, alquiler)

grilla_x = np.linspace(start = 0, stop = 200, num = 1000)
grilla_y = grilla_x*a + b


g = plt.scatter(x = superficie, y = alquiler)
plt.title('precio_alquiler ~ superficie')
plt.plot(grilla_x, grilla_y, c = 'green', label = 'ajuste lineal')
plt.xlabel('Superficie')
plt.ylabel('Alquiler')
plt.legend()
plt.show()