import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()


def caminatas_aleatorias(n, N):
    '''genera n caminatas aleatorias de N pasos.
    pre: n,N enteros positivos
    pos: devuelve un array de caminatas aleatorias
    '''
    caminatas = [randomwalk(N) for i in range(n)]
    arr = np.array(caminatas)
    return arr


def alejados(arr_caminatas):
    '''calcula los valores maximos en valor absoluto de los elementos del iterable y devuelve una tupla con el elemento min y el elemento maximo
    pre: recibe un iterable
    pos: retorna una tupla con el valor minimo y el valor maximo, de los maximos del iterable
    '''
    maximos = []
    for caminata in arr_caminatas:
        abs_array = np.absolute(caminata)
        maximos.append(max(abs_array))
    
    mas_alejado_index = maximos.index(max(maximos))
    menos_alejado_index = maximos.index(min(maximos))

    return arr_caminatas[menos_alejado_index], arr_caminatas[mas_alejado_index]


def f_principal():
    N = 100000

    caminatas = caminatas_aleatorias(12, N)

    plt.figure()
    #12 caminatas al azar
    plt.subplot(2, 1, 1)

    for i in caminatas:
        plt.plot(i)

    plt.ylim(-1000, 1000)
    plt.xticks([])
    plt.yticks([-500,0,500])
    plt.title("12 Caminatas al azar")
    
    # la caminata que mas se aleja
    plt.subplot(2, 2, 3) 
    plt.plot(alejados(caminatas)[1])
    plt.ylim(-1000, 1000)
    plt.xticks([])
    plt.yticks([-500,0,500])
    plt.title("La caminata que mas se aleja")
    #la caminata que menos se aleja
    plt.subplot(2, 2, 4) 
    plt.plot(alejados(caminatas)[0])
    plt.ylim(-1000, 1000)
    plt.xticks([])
    plt.yticks([])
    plt.title("La caminata que menos se aleja")

    plt.show()

if __name__ == '__main__':
    f_principal()