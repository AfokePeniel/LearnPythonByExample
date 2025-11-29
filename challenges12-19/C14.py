'''Ask the user to enter a number between 10 and 20 (inclusive). If they enter a
number within this range, display the message “Thank you”, otherwise display the
message “Incorrect answer”.
'''

#Solution

numb1 = int(input("Enter any number between 10 to 20: "))
if numb1 in range(10, 21):
    print("Thank you")
else:
    print("Incorrect answer")
    