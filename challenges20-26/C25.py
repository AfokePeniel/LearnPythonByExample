'''
Ask the user to enter their first name. If the length 
of their first name is under five characters, ask them to enter their surname and join them
together (without a space) and display the name 
in upper case. If the length of the first name is five 
or more characters, display their first name in lower case.
'''

#Solution

f_name = input("Enter your first name: ")
d_f_name = len(f_name)

if d_f_name <= 5 :
    s_name = input("Enter your surname: ")
    name = f_name+s_name
    print(name)
elif d_f_name > 5:
    print(f_name.lower())
    
