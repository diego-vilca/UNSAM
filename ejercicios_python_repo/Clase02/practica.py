##Archivos

##LECTURA

# f = open('../Data/arboles.csv','rt') # 'r' de read, 't'de text
# data = f.read()
# print(data)

# f.close()
#============================================================================================


# ruta_archivo = '../Data/arboles.csv'
# #Cuando utilizo with open no es necesario cerrarlo
# with open(ruta_archivo, 'rt', encoding='utf8') as archivo:
#     for i, linea in enumerate(archivo):
#         print(i, linea)

#============================================================================================

# f = open('../Data/arboles.csv','rt', encoding='utf8')
# #next mueve el puntero a la linea siguiente del texto, de esta manera puedo recuperar solo los encabezados
# #split devuelve una lista separadas por el iterador seleccionado
# encabezados = next(f).split(',')
# print(encabezados) 

# #el puntero quedo en la segunda linea, ahora las recorro e imprimo
# for line in f:
#     fila = line.split(',')
#     print(fila)
# f.close()

#============================================================================================
## Si estás trabajando con archivos enormes es mejor procesar las líneas de tu archivo una a una.
# with open('../Data/camion.csv', 'rt') as f:
#         for line in f:
#             print(line, end = '')


#============================================================================================
##ESCRITURA

# # with open('../Data/test.txt', 'wt') as out:
# #     out.write('Hello world\n')

# with open('outfile', 'wt') as out:  #si el archivo no existe lo crea
#     print('Hola a todos', file=out)
#     # print('Hola a todos', file=out, end = '')   #por defecto el parametro end es \n (salto de linea)

#============================================================================================
