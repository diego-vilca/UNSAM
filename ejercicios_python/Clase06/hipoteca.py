
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
