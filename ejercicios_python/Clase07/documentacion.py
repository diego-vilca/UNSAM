def valor_absoluto(n):
    '''devuelve la distancia del valor al cero

    pre: recibe un valor númerico
    pos: devuelve el valor absoluto
    '''
    if n >= 0:
        return n
    else:
        return -n

#======================================================================

def suma_pares(l):
    '''suma los valores pares de una lista

    pre: recibe una lista de valores númericos
    pos: retorna la sumatoria de los elementos pares de la lista
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
# inv: res acumula la sumatoria de los elementos pares de la lista que ya fueron analizados

#======================================================================

def veces(a, b):
    '''suma el valor a una cantidad de veces b

    pre: a y b deben ser valores númericos con b >= 0
    pos: retorno a * b
    '''
    res = 0
    nb = b
    while nb != 0:
        print(nb * a + res)
        res += a
        nb -= 1
    return res
#inv: res = a * (b - nb)

#======================================================================

def collatz(n):
    '''Si el número es par, se divide entre 2. Si el número es impar, se multiplica por 3 y se suma 1.

    pre: n debe ser un entero positivo
    pos: devuelve la cantidad de veces que se evalua la condicion del ciclo
    '''
    res = 1

    while n!=1:
        print(f"res={res}, n={n}")
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
#inv: res >= 1 y n >= 1