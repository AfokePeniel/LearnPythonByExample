'''
Update program C27 so that it will display the answer to
two decimal places.
'''

#Solution

import math

numb = float(input("Enter a decimal number: "))
final_numb = numb * 2

#print(final_numb)

print(round(final_numb, 2))