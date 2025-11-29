'''Ask for two numbers. If the first one is larger than the second, display the second number first
and then the first number, otherwise show the first number first and then the second.'''

#Solution

numb1 = int(input("Enter the first number: "))
numb2 = int(input("Enter the second number: "))

if numb1 > numb2:
    print(numb2)
    print(numb1)
else:
    print(numb1)
    print(numb2)
    
    