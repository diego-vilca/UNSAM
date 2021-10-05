from datetime import datetime, timedelta

def fecha_reincorporacion(inicio_licencia):
    '''calcula la fecha de reincorporacion a partir de la fecha de inicio de la licencia
    pre: cadena con la fecha de inicio con formato '%d/%m/%Y'.
    post: devuelve una cadena con la fecha de reincorporacion pasados 200 dias.
    '''
    f_inicio = datetime.strptime(inicio_licencia, '%d/%m/%Y')
    reincorporacion = f_inicio + timedelta(days = 200)

    return reincorporacion.strftime('%d/%m/%Y')
