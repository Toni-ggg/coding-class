income = int(input('please enter your monthly income: '))
age = int(input('please enter your age: '))
spending_habits= input('please enter your spending habits: ')


per=0.2 * income

total = 0



a = income * 0.1 +  income

b = a * 0.1 + a

c = b * 0.1 + b

d = c * 0.1 + c

e = d * 0.1 + d

if income < 2000:
    if age > 20<40:
        if spending_habits == 'high':
            print('Basic savings plan:You need to save:417E,each month to reach 10k in 2 years')
        
        else:
            print('flexible budget plan - gives tips on saving and investing your money')
        
    else:
        print('flexible budget plan - gives tips on saving and investing your money')
        
elif income > 5000:
    if age < 30:
        if spending_habits=='low':
            print('aggresive savings plan-projected savings in 5 years with 10 percent yearly return',e)
        else:
            print('flexible budget plan - gives tips on saving and investing your money')
    else:
        print('flexible budget plan - gives tips on saving and investing your money')
            
elif income >2000<5000:
    if spending_habits == 'moderate':
        print('Standard savings plan,you need to save',per)
    else:
        print('flexible budget plan - gives tips on saving and investing your money')
else:
    print('flexible budget plan - gives tips on saving and investing your money')        

    