'''
Ask how many slices of pizza the user started with and ask how many slices
they have eaten.
Work out how many slices they have left and display the answer in a userfriendly format.
'''

#Solution

pizza_slice = int(input("How many slices of Pizza are they?: \n"))
eaten_pizza = int(input("How many slices of Pizza have you eaten?: \n"))
answer = pizza_slice - eaten_pizza

print("There are" + " " + str(answer) + " " + "slices of pizza left")