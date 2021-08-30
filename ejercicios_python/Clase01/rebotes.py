#rebotes.py

# Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5
# de la altura desde la que cayó. Escribí un programa rebotes.py que imprima una tabla mostrando las
# alturas que alcanza en cada uno de sus primeros diez rebotes.
# Nota: Podés limpiar un toque la salida si usás la función round() de la que miraste el help hace un rato. 
# Tratá de usarla para redondear a cuatro dígitos.

altura = 100

for i in range(1, 11):
    altura = altura * 3/5
    print(i, round(altura, 4))