ab = input('Enter the lenght of a-b: ')
ab = float(ab)
bc = input('Enter the lenght of b-c: ')
bc = float(bc)
cd = input('Enter the lenght of c-d: ')
cd = float(cd)
da = input('Enter the lenght of d-a: ')
da = float(da)
i = input('Enter the angle of i: ')
i = float(i)
if ab == cd:
    if bc == da:
        if i == 90:
            print('Its a square')
        else:
            print('Its a rhombus')
    else:
        print('Its an irregular quadrilateral')
else:
    print('Its an irregular quadrilateral')
    if ab == cd:
        if bc == da:
            if i ==90:
                print('Its a rectangle')
            else:
                print('Its a parallelogram')
        else:
            print('Its an irregular qyadrilateral')
    else:
        print('Its an irregular quadrilateral')
    
    
        
            