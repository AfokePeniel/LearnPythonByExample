'''
Ask the user to enter an integer that is over 500. Work
out the square root of that number and display it to two decimal places.
'''

#Solution

import math

numb = int(input("Enter any number greater than 500: "))
final_numb = math.sqrt(numb)
print(round(final_numb, 2))