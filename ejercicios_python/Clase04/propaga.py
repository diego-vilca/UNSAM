
#%%
def propagar(vector):
    lista = []
    lista = list(vector)
    

    for i, e in enumerate(lista):
        
        # Busco el fosforo encendido
        if e == 1:
            # recorro los fosforos de la derecha
            for s in range(i + 1, len(vector), 1):
                # si encuentro uno carbonizado dejo de quemar
                if lista[s]  == -1:
                    break
                else: # ...sino quemo
                    lista[s] = 1  
            # recorro hacia la izquierda
            for t in range(i - 1, -1, -1):
                # si encuentro uno carbonizado dejo de quemar
                if lista[t]  == -1:
                    break
                else: # ...sino quemo
                    lista[t] = 1  
            
    return lista   

# lista = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
# lista = [ 0, 0, 0, 1, 0, 0]
# lista = [-1, 0, 0, 0, -1, 0, 0, 1, 0, -1, -1, 0, 1]
# print(propagar(lista))