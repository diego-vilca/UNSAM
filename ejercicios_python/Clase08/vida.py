# Ejercicio 8.1: Segundos vividos
# Escribí una función llamada vida_en_segundos(fecha_nac) a la que le pasás tu fecha de nacimiento y 
# te devuelve la cantidad de segundos que viviste (asumiendo que naciste a las 00:00hs de tu fecha de nacimiento).

from datetime import datetime

def vida_en_segundos(fecha_nac):
    '''Devuelve la cantidad de segundos pasados de tu vida

    pre: recibe la fecha de nacimiento en una cadena con formato '%d/%m/%Y'   
    post: retorna la cantidad de segundos pasados a partir de la fecha de nacimiento
    '''
    fecha_nacimiento = datetime.strptime(fecha_nac, '%d/%m/%Y')
    fecha_actual = datetime.now()
    fecha_segundos = (fecha_actual - fecha_nacimiento).total_seconds()

    return fecha_segundos