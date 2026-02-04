dyw = input('Enter what degrees you want to convert(fahrenheit to celsius(fc),or celsius to fahrenheit(cf): ')
temp = input('Enter the temperature: ')
temp = float(temp)













if (dyw == 'cf'):
    print('the temprature converted to fahrenheit is:',temp * 9 / 5 + 32 )
elif (dyw == 'fc'):
    print('the temprarture converted to celsius is:',(temp - 32) * 5 / 9)
else:
    print('ERROR')
    
    