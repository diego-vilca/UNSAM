#Ejercicio 8.9: Comparando especies en parques y en veredas

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1
df_parques = pd.read_csv(os.path.join('../Data', 'arbolado-en-espacios-verdes.csv'))
df_veredas = pd.read_csv(os.path.join('../Data', 'arbolado-publico-lineal-2017-2018.csv'))
#2
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][['altura_tot', 'diametro', 'nombre_cie']].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']].copy()

df_tipas_parques.rename(columns = {'altura_tot' : 'altura', 'diametro' : 'diametro_altura_pecho', 'nombre_cie' : 'nombre'}, inplace = True)
df_tipas_veredas.rename(columns = {'altura_arbol' : 'altura' , 'nombre_cientifico' : 'nombre'}, inplace = True)
#3
df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'
#4
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
#5
df_tipas.boxplot('diametro_altura_pecho', by = 'ambiente')
plt.show()
#6
df_tipas.boxplot('altura', by = 'ambiente')
plt.show()

#7
#Se podria utilizar una funcion cuyo parametro sea el nombre_cientifico de la especie y utilizar esta variable para crear el nuevo dataframe, por ejemplo:
#
#    df_arbol_parques = df_parques[df_parques['nombre_cie'] == nombre_cientifico][['altura_tot', 'diametro', 'nombre_cie']].copy()
#    df_arbol_veredas = df_veredas[df_veredas['nombre_cientifico'] == nombre_cientifico][['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']].copy()
#
#Es el unico cambio que deberia hacerse ya que los demas pasos aplican para tosdos los arboles



