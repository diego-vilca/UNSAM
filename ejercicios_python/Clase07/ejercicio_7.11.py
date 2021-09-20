import matplotlib.pyplot as plt

fig = plt.figure()
plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva, los puntos son: (0,0),(1,1),(2,0)
plt.xticks([]), plt.yticks([]) # saca las marcas
# como la primer figura abarca 3 lugares la que le sigue es indice 4
plt.subplot(2, 3, 4) 
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5) 
plt.plot([0,0])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6) 
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()
