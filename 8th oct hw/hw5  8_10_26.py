ms = input('please enter your monthly sales: ')
ms = float(ms)

commision_of_15 = 15 * ms

commision_of_5 = 5 * ms

if ms > 40000:
    print('your commision is 15% of what you sold: ',commision_of_15)
else:
    print('your commision is 5% of what you sold: ',commision_of_5)