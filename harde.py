a_range = input('Enter a integer: ')
a_range =int(a_range)
b_range = input('Enter another integer: ')
b_range =int(b_range)
c_range = input('Enter another integer: ')
c_range =int(c_range)
for a in range(1,a_range):
    for b in range(1,b_range):
        for c in range(1,c_range):    
            asq = a * a
            bsq =  b * b
            csq = c * c 
            asqplusbsq = asq + bsq
            if asqplusbsq == csq:
                print('You have entered the pythagorean triples',a,b,c)
    
