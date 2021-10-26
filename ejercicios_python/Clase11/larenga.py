# Ejercicio 11.9: Pascal
def pascal(n, k):
    if k == 0: #primera columna
        return 1
    elif n == 0: #primera fila, con k != 0 
        return 0
    else:
        res = pascal(n-1, k) + pascal(n-1, k-1)
        return res