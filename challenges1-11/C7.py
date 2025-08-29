'''
Ask the user for their name and their age. Add 1 to their age
and display the output [Name] next birthday you
will be [new age].

'''

#Solution

user_name = input("Kindly enter your name: \n")
user_age = int(input("Kindly enter your age: \n"))
new_age = user_age + 1
print( user_name, "by your next birthday, you will be" + " " + str(new_age))