height = input('Enter the height of your cylinder: ')
height = float(height)
radius = input('Enter the radius of the prism: ')
radius = float(radius)
PI = 3.14
area_part_1 = height * radius * PI * 2
area_part_2 =  2 * PI *radius * radius
total_surface_area = area_part_1 + area_part_2
print('the surface area of your cylinder is: ',total_surface_area,'units squared')