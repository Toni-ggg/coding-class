number1 = input('enter  number1: ')
number1= float(number1)
number2 = input('enter number 2: ')
number2  = float(number2)
number3 = input('enter number 3: ')
number3 = float(number3)

if number1 > number3:
    if number1 > number2:
        print('the largest number is',number1)
    
if number2 > number1:
    if number2 > number3:
        print('the largest number is',number2)
    
    
if number3 > number2:
    if number3 > number1:
        print('the largest number is',number3)
    


