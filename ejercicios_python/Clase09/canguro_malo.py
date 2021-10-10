# # canguro_malo.py
# """Este código continene un 
# bug importante y dificil de ver

# RESPUESTA: El error se encontraba en el parámetro opcional del método constructor, al cual por defecto se le asignaba un valor mutable.
# Los parametros opcionales solo se evaluan cuando la definición de la función se ejecuta, por lo que si modificamos el valor mutable del objeto 
# también modificamos el valor del parametro por defecto y, como comparten referencia, la proxima vez que instanciemos un objeto el nuevo valor por 
# defecto sera el modificado.
# """

# class Canguro:
#     """Un Canguro es un marsupial."""
    
#     def __init__(self, nombre, contenido = None):
#         """Inicializar los contenidos del marsupio.

#         nombre: string
#         contenido: contenido inicial del marsupio, lista.
#         """
#         if contenido is None:
#             contenido = []

#         self.nombre = nombre
#         self.contenido_marsupio = contenido

#     def __str__(self):
#         """devuelve una representación como cadena de este Canguro.
#         """
#         t = [ self.nombre + ' tiene en su marsupio:' ]
#         for obj in self.contenido_marsupio:
#             s = '    ' + object.__str__(obj)
#             t.append(s)
#         return '\n'.join(t)

#     def meter_en_marsupio(self, item):
#         """Agrega un nuevo item al marsupio.

#         item: objecto a ser agregado
#         """
#         self.contenido_marsupio.append(item)

# #%%
# madre_canguro = Canguro('Madre')
# cangurito = Canguro('gurito')
# madre_canguro.meter_en_marsupio('billetera')
# madre_canguro.meter_en_marsupio('llaves del auto')
# madre_canguro.meter_en_marsupio(cangurito)

# print(madre_canguro)
# print(cangurito)
# # Al ejecutar este código todo parece funcionar correctamente.
# # Para ver el problema, imprimí el contenido de cangurito.
