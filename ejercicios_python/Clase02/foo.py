##Atrapar y administrar excepciones

# numero_valido=False
# while not numero_valido:
#     try:
#         a = input('Ingresá un número entero: ')
#         n = int(a)
#         numero_valido = True
#     except ValueError:
#         print('No es válido. Intentá de nuevo.')
# print(f'Ingresaste {n}.')

# numero_valido=False
# while not numero_valido:
#     try:
#         a = input('Ingresá un número entero: ')
#         n = int(a)
#         numero_valido = True
#     except:
#         print('No es válido. Intentá de nuevo.')
# print(f'Ingresaste {n}.')

#============================================================================================

##Generar excepciones

# raise RuntimeError('¡Qué moco!')

#============================================================================================

def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad