# Ejercicio 1.18: Geringoso rústico
# Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.

cadena = 'Geringoso'
capadepenapa = ''
cadena = cadena.lower()

for c in cadena:

    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        capadepenapa = capadepenapa + c + 'p'+ c
    else:
        capadepenapa = capadepenapa + c

    
capadepenapa = capadepenapa.capitalize()
print(capadepenapa)
