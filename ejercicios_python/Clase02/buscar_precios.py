# Ejercicio 2.7: Buscar precios
# A partir de lo que hiciste en el Ejercicio 2.3, escribí una función buscar_precio(fruta) que busque en archivo ../Data/precios.csv 
# el precio de determinada fruta (o verdura) y lo imprima en pantalla. Si la fruta no figura en el listado de precios,
#  debe imprimir un mensaje que lo indique.

def buscar_precio(fruta):

    precio = 0.0
    se_encontro = False
    #Por si el usuario ingresa la palabra en minusculas o en mayusculas..
    fruta = fruta.lower()
    fruta = fruta.capitalize()

    with open('../Data/precios.csv', 'rt', encoding='utf8') as f:
        for line in f:
            row = line.split(',')
            if row[0] == fruta:
                precio = float(row[1])
                se_encontro = True
                print(f'El precio de un cajón de {fruta} es: {precio}')
        
        if not se_encontro:
            print(f'{fruta} no figura en el listado de precios.')
    
         

buscar_precio('Frambuesa')
buscar_precio('Kale')



