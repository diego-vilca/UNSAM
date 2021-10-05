from datetime import datetime, timedelta

def dias_habiles(inicio, fin, feriados):
    ''' devuelve los días habiles entre dos fechas, teniendo en cuenta feriados.
    pre: recibe el rango de fechas (inicio-fin) en cadenas, y una lista con feriados.
    post: devuelve una lista con los días habiles dentro del periodo ingresado, incluyendo las fechas de inicio y fin.
    '''
    l_habiles = []
    f_inicio = datetime.strptime(inicio, '%d/%m/%Y')
    f_fin = datetime.strptime(fin, '%d/%m/%Y')
    
    fechas = datetime( year= f_inicio.year, month= f_inicio.month, day= f_inicio.day)

    #agrego la fecha de inicio a la lista
    l_habiles.append(fechas.strftime('%d/%m/%Y'))
    fechas = fechas + timedelta(days = 1)

    #agrego dias habiles a la lista
    while fechas < f_fin:
        if fechas.weekday() != 5 and fechas.weekday() != 6 and fechas.strftime('%#d/%m/%Y') not in feriados:   # El '#' dentro del formato del strftime en el día, es para ignorar el prefijo cero en números de un digito
            l_habiles.append(fechas.strftime('%d/%m/%Y'))
        fechas = fechas + timedelta(days = 1)

    #agrego la fecha final a la lista
    l_habiles.append(f_fin.strftime('%d/%m/%Y'))
    
    return l_habiles

