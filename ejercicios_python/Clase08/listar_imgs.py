import os
from pprint import pprint

def archivos_png(directorios):
    l_png = []

    for root, dirs, files in os.walk(directorios):
        for file in files:
            if file.endswith('.png'):
                l_png.append(file)

    return l_png


def f_principal(argv):
    if len(argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'un_directorio')
    directorio = argv[1]
    pprint(archivos_png(directorio))


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
