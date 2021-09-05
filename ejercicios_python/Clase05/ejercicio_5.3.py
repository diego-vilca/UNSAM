# Ejercicio 5.3: Cocumpleaños
# Haciendo miles de experimentos numéricos, estimá la probabilidad de que en un grupo de 30 personas elegidas al azar, dos cumplan años el mismo día. 
# Escribí un programita que permita calcular esa probabilidad asumiendo que el año tiene 365 días.

from pprint import pprint
import random
from collections import Counter

def cocumpleaños(N):
    cumples = []
    dias = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    meses = ['Ene','Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    coincidencia = 0

    # asigno las fechas de cumpleaños
    for i in range(N):

        mes = random.choice(meses)

        if mes =='Ene' or  mes =='Mar' or  mes =='May' or  mes =='Jul' or  mes =='Ago' or mes =='Oct' or  mes =='Dic':
            dia = random.choice(dias)
        elif mes =='Abr' or mes =='Jun' or  mes =='Sep' or  mes =='Nov':
            dia = random.choice(dias[0:30])
        else:
            dia = random.choice(dias[0:28])

        cumples.append((dia, mes))

    cumples = Counter(cumples)
    # 
    for i in cumples:
        if cumples[i] == 2: # Podria ser >= 2 ???
            coincidencia += 1
    
    print(f"coincidencias: {coincidencia}")
    pprint(cumples)

    prob = coincidencia/N

    return prob
