# Ejercicio 3.17: Tablas de multiplicar
# Escribí un programa tablamult.py que imprima de forma prolija las tablas de multiplicar del 1 al 9 usando f-strings. 
# Si podés, evitá usar la multiplicación, usando sólo sumas alcanza.

def multiplicar():
    lista = []

    for y in range(0, 10):
        cadena = ''
        resultado = 0
        primer_columna = f'{y:d}:'

        # Creo el encabezado de la tabla
        if y == 0:
            for i in range(0, 10):
                if i == 0:
                    cadena += f'{i:>8d}'
                else:
                    cadena += f'{i:>4d}'
            cadena += '\n'
            # creo el separador
            cadena += f'{"-" * 45}' + '\n'

              
        for x in range(0, 9):
            # concateno la primer columna y los ceros al principio de cada fila
            if x == 0:
                cadena += f'{primer_columna:^4}' f'{x:>4d}'
            # creo la primer fila de ceros
            if y == 0:
                cadena += f'{y:>4d}'
            # creo el resto de las filas
            else:
                resultado = resultado + y

                cadena += f'{resultado:>4d}'

        lista.append(cadena)

    # Recorro la lista e imprimo cada una de las filas de la tabla
    for resultado in lista:
        print(resultado)        





print('\n')

# Llamo a la funcion
multiplicar()

print('\n')

