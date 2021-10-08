class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        print('%10s %10s %10s %10s' % headers)
        print(('-'*10 + ' ')*len(headers))
        raise NotImplementedError()
    
    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        print('%10s %10d %10.2f %10.2f' % rowdata)
        raise NotImplementedError()



class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()