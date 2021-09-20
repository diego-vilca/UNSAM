# fileparse.py
import csv

def parse_csv(iterable, select = None, types = None, has_headers = True, silence_errors = False):
    
    # asigno las lineas del iterable de entrada al iterable 'filas'
    filas = csv.reader(iterable)

    if has_headers:

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []


        registros = []

        
        for i, fila in enumerate(filas, start=1):
            try:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                #Parseo los datos
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]

                # Armar el diccionario
                registros.append(dict(zip(encabezados, fila)))

            #si falta algun dato en la fila, manejo la excepcion del parseo de datos
            except ValueError as e:
                if not silence_errors:
                    print(f"Fila {i}: No pude convertir {fila}")
                    print(f"Fila {i}: Motivo: {e}")

    #si no hay encabezados...
    else:
        #si los parametros select y has_headers = false son pasados juntos, lanzo una excepcion.
        if select:
            raise RuntimeError("Para seleccionar, necesito encabezados.")

        registros = []
        
        for i, fila in enumerate(filas, start=1):
            try:
                if not fila:    # Saltear filas vacías
                    continue

                if types:
                    fila = [ func(val) for func, val in zip(types, fila) ]

                # transformo la lista en tupla
                registros.append(tuple(fila))

            #si falta algun dato en la fila, manejo la excepcion
            except ValueError as e:
                if not silence_errors:
                    print(f"Fila {i}: No pude convertir {fila}")
                    print(f"Fila {i}: Motivo: {e}")

    return registros