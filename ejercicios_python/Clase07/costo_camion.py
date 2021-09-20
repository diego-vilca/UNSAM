# Copiá el archivo costo_camion.py al directorio de la clase actual y actualizalo para que ahora importe informe_final 
# en vez de informe_funciones. Luego, modificalo para que incluya una función similar f_principal()

import informe_final

def costo_camion(nombre_archivo):
    total = 0.0
    camion = informe_final.leer_camion(nombre_archivo)

    for fruta in camion:
        total += fruta['cajones'] * fruta['precio']

    return total


def f_principal(argv):
    if len(argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion')
    camion = argv[1]
    print(f'Costo total: {costo_camion(camion)}')


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)



    
