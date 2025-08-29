'''
Task the user to enter a number over 100 and then enter a number under 10 and 
tell them how many times the smaller number goes into the larger number in a user-friendly format.
'''

#Solution

abv_hun = int(input("Enter any number above 100: "))
under_ten = int(input("Enter any number under 10: "))
answer = abv_hun // under_ten

print(under_ten, "goes into" , abv_hun,": " + str(answer) + " times.")