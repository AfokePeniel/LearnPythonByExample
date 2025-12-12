'''
Ask the user to enter two numbers.
Use whole number division to divide
the first number by the second and
also work out the remainder and
display the answer in a user-friendly
way (e.g. if they enter 7 and 2 display
“7 divided by 2 is 3 with 1
remaining”).
'''

# Solution

numb1 = int(input("Enter the first number: "))
numb2 = int(input("Enter the second number: "))
div = numb1 // numb2
divv = numb1 % numb2

print(f"{numb1} divided by {numb2} is {div} with {divv} remaining")