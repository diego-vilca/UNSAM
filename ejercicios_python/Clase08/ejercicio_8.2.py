# Ejercicio 8.2: Cuánto falta para la primavera
from datetime import date

def dias_para_primavera():
    '''Devuelve los dias que faltan para la primavera, si nos encontramos en un dia de la estación devuelve cero
    pre: ninguna
    post: Devuelve un entero con los días que faltan para primavera
    '''
    hoy = date.today()

    if hoy.month <= 9 and hoy.day < 21:
        falta = date(year = hoy.year(), month = 9, day = 21) - hoy
        falta = falta.days

    elif hoy.month == 12 and hoy.day >= 21:
        falta = date(year = hoy.year() + 1, month = 9, day = 21) - hoy
        falta = falta.days

    else:
        falta = 0

           
    return falta


