# Ejercicio 5.7: arange() y linspace()
# Generá un vector que tenga los números impares entre el 1 y el 19 inclusive usando arange(). 
# Repetí el ejercicio usando linspace(). ¿Qué diferencia hay en el resultado?

import numpy as np

a = np.arange(1, 20, 2)

print(a)

b = np.linspace(1, 19, 10)

print(b)

c = np.linspace(1, 19, 10, dtype=np.int64)

print(c)