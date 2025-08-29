'''
Ask the user to enter three
numbers. Add together the first
two numbers and then multiply
this total by the third. Display the
answer as The answer is
[answer].
'''

# Solution
numb1 = int(input("Enter the first number: \n"))
numb2 = int(input("Enter the second number: \n"))
numb3 = int(input("Enter the third number: \n"))

total = numb1 + numb2
answer = total * numb3

print("The answer is ", answer)
