# Escribí un código que abra el archivo Data/precios.csv, busque el precio de la naranja y lo imprima en pantalla.

precio = 0.0

with open('../Data/precios.csv', 'rt', encoding='utf8') as f:
    for line in f:
        row = line.split(',')
        if row[0] == 'Naranja':
            precio = float(row[1])

print('El precio de la naranja es:', precio)