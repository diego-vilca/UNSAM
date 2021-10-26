# def sumar(lista):
#     '''Devuelve la suma de los elementos en la lista'''
#     res = 0
#     if len(lista) != 0:
#         res = lista[0] + sumar(lista[1:])
#     return res

# def sumar(lista, suma=0):
#     '''Devuelve la suma de los elementos en la lista'''
#     res = suma
#     if len(lista) != 0:
#         res = sumar(lista[1:], lista[0] + suma)
#     return res

# def pascal(n,k):
#     def pascal_aux(n):
#         if n == 0:
#             return []
#         elif n == 1:
#             return [1]
#         else:
#             fila = [1]
#             res = pascal(n-1)

# def pascal(n):
#     def pascal_aux(n):
#         if n == 0:
#             print('CASO 0')
#             return []
#         elif n == 1:
#             print('CASO 1')
#             return [1]
#         else:
#             fila_nueva = [1]
#             print(f' {n}', end='')
#             res = pascal_aux(n-1)
#             print(res)
#             return res

#     return pascal_aux(n)

# def pascal(n, k):
#     if k == 0:
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         return pascal(n-1, k) + pascal(n-1, k-1)

# def bbinaria_rec(lista, e):
#     if len(lista) == 0:
#         print('Lista vacia')
#         res = False
#     elif len(lista) == 1:
#         print(f'Unico elemento')
#         print(f'{lista[0]}')
#         res = lista[0] == e
#     else:
#         medio = len(lista)//2

#         # completar
#         if lista[medio] == e:
#             print('Entreee')
#             print(f'{lista[medio]}')
#             res = True

#         elif lista[medio] > e:
#             # lista = lista[:medio]
#             print(f'{medio} > e')
#             print(f'lista: {lista}')
#             res = bbinaria_rec(lista[:medio], e)
#         else:
#             # lista = lista[medio+1:]
#             print(f'{medio} > e')
#             print(f'lista: {lista}')
#             res = bbinaria_rec(lista[medio+1:], e)

#     return res

# def medidas_hoja_A(N):
#     if N == 0:
#         ancho = 841
#         largo = 1189

#         return ancho, largo

#     ancho, largo = medidas_hoja_A(N-1)

#     return largo//2, ancho



import numpy as np
import matplotlib.pyplot as plt


def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b


superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])








