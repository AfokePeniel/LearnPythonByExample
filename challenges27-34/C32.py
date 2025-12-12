'''
Ask for the radius and the depth of a cylinder
and work out the total volume (circle
area*depth) rounded to three decimal
places.
'''

#Solution

import math

radi = float(input("Enter the radius of a circle: "))
depth = float(input("Enter the depth of a cylinder: "))
area = math.pi * (radi ** 2)

total_vol = area * depth

print(round(total_vol, 3))