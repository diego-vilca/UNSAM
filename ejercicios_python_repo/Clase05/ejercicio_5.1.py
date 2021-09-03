import random


def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    # print(tirada)
    return tirada


def es_generala(tirada):
    for i in range(len(tirada)):
        if tirada[i] != tirada[0]:
            return False
    return True


N = 100000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')