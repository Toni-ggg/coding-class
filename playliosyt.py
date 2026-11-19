mood=input('please enter how your felling: ')
weather =input('please enter the weather outside:')
if mood == 'happy':
    if weather =='sunny':
        print('pop hits')
    if weather == 'not sunny':
        print('top charts')
elif mood == 'sad':
    if weather == 'rainy':
        print('sad acoustic')
    if weather == 'not rainy':
        print('top charts')
elif mood == 'relaxed':
    print('chill vibes')



else:
    print('top charts')

        