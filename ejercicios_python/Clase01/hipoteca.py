# hipoteca.py

# Ejercicio 1.7: La hipoteca de David
# David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%. 
# Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.

# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0


# while saldo > 0:
#     saldo = saldo * (1+tasa/12) - pago_mensual
#     total_pagado = total_pagado + pago_mensual


# print('Total pagado', round(total_pagado, 2))

#===========================================================================================================================================
#===========================================================================================================================================


# Ejercicio 1.8: Adelantos
# Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.
# Modificá el programa para incorporar estos pagos extra y que imprima el monto total pagado junto con la cantidad de meses requeridos.

# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# mes = 0
# meses_abonados = 0


# while saldo > 0:
    
#     if  mes < 12:
#         saldo = saldo * (1+tasa/12) - pago_mensual - 1000
#         total_pagado = total_pagado + pago_mensual + 1000
#     else:
#         saldo = saldo * (1+tasa/12) - pago_mensual
#         total_pagado = total_pagado + pago_mensual
    
#     mes += 1


# print(f'Total pagado {round(total_pagado, 2)} en {mes} meses')

#===========================================================================================================================================
#===========================================================================================================================================

# Ejercicio 1.9: Calculadora de adelantos
# ¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?

# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# mes = 0
# pago_extra_mes_comienzo = 61
# pago_extra_mes_fin = 108
# pago_extra = 1000


# while saldo > 0:
#     if mes >= pago_extra_mes_comienzo and mes < pago_extra_mes_fin + 1:
#         saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
#         total_pagado = total_pagado + pago_mensual + pago_extra
#     else:
#         saldo = saldo * (1+tasa/12) - pago_mensual
#         total_pagado = total_pagado + pago_mensual

#     mes += 1


# print(f'Total pagado {round(total_pagado, 2)} en {mes} meses')


#===========================================================================================================================================
#===========================================================================================================================================

# Ejercicio 1.10: Tablas
# Modicá tu programa para que imprima una tabla mostrando el mes, el total pagado hasta el momento y el saldo restante.

# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# mes = 1
# pago_extra_mes_comienzo = 61
# pago_extra_mes_fin = 108
# pago_extra = 1000


# while saldo > 0:
#     if mes >= pago_extra_mes_comienzo and mes < pago_extra_mes_fin + 1:
#         saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
#         total_pagado = total_pagado + pago_mensual + pago_extra
#     else:
#         saldo = saldo * (1+tasa/12) - pago_mensual
#         total_pagado = total_pagado + pago_mensual

#     mes += 1

#     print(f'{mes} {round(total_pagado, 2)} {round(saldo, 2)}')


# print(f'Total pagado: {round(total_pagado, 2)} \nMeses: {mes - 1}') #para usar 'mes' como contador le resto 1


#===========================================================================================================================================
#===========================================================================================================================================

#Ejercicio 1.11: Bonus
# Ya que estamos, corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 1
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000


while saldo > 0:

    if mes >= pago_extra_mes_comienzo and mes < pago_extra_mes_fin + 1:
         #si la deuda mensual es menor que el pago mensual, solo pago lo que adeudo
        if saldo * (1+tasa/12) < pago_mensual:
            pago_mensual = saldo * (1+tasa/12)

        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
    else:
        #si la deuda mensual es menor que el pago mensual, solo pago lo que adeudo
        if saldo * (1+tasa/12) < pago_mensual:
            pago_mensual = saldo * (1+tasa/12)
        
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual

    mes += 1

    #para usar 'mes' como contador le resto 1
    print(f'{mes - 1} {round(total_pagado, 2)} {round(saldo, 2)}')


print(f'Total pagado: {round(total_pagado, 2)} \nMeses: {mes - 1}') 
