# Ejercicio 4.5: Invertir una lista
# Escribí una función invertir_lista(lista) que dada una lista devuelva otra que tenga los mismos elementos pero en el orden inverso. 
# Es decir, el que era el primer elemento de la lista de entrada deberá ser el último de la lista de salida y análogamente con los demás elementos.

def invertir_lista(lista):
    invertida = []
    
    for i in range(len(lista)-1, -1, -1):
        invertida.append(lista[i])
    
    return invertida

'''
solucion que da el video:

    def invertir_lista(lista):
        invertida = []
        for e in lista:
            invertida = [e] + invertida
        return invertida

'''