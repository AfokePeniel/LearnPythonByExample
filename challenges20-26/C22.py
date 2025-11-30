'''
Ask the user to enter their first name and surname in lower
case. Change the case to title case and join them together.
Display the finished result.
'''

#Solution

f_name = input("Enter your first name: ").lower()
s_name = input("Enter your surname: ").lower()

display = f_name+s_name
print(display.title())