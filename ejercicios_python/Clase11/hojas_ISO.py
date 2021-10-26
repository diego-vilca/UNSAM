# Ejercicio 11.13: Hojas ISO y recursión
def medidas_hoja_A(N):
    if N == 0:
        ancho = 841
        largo = 1189

        return ancho, largo

    ancho, largo = medidas_hoja_A(N-1)
    
    return largo//2, ancho
