sp = input('Enter the sale price: ')
sp = int(sp)
sr = input('Enter the sale region(national or foreign): ')
national = 'national'
foreign = 'foreign'
if sr == national:
    print('Your total price is: ',sp * 0.08 + sp)
elif sr == foreign:
    print('Your total price is: ',sp * 0.18 + sp)
else:
    print('ERROR')


