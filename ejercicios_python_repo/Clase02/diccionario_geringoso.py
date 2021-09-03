# Ejercicio 2.14: Diccionario geringoso.
# Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso. 
# Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus traducciones 
# al geringoso (como en el Ejercicio 1.18). Probá tu función para la lista ['banana', 'manzana', 'mandarina']

#================================================================
#traductor geringoso

def traductor(palabra):
    traduccion = ''
    for c in palabra:
        if c in 'aeiou':
            traduccion = traduccion + c + 'p'+ c
        else:
            traduccion = traduccion + c
    
    return traduccion

#================================================================
#DICCIONARIO GERINGOSO

def diccionario(lista):
    d = {}
    
    for palabra in lista:
        d[palabra] = traductor(palabra)
    
    return d

#================================================================

lista = ['banana', 'manzana', 'mandarina']
print(diccionario(lista))

