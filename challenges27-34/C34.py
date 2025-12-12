'''
Display the following message:
   1) Square
   2) Triangle
   Enter a number: 
   
If the user enters 1, then it should ask them for
the length of one of its sides and display the
area. If they select 2, it should ask for the base
and height of the triangle and display the area. If
they type in anything else, it it should give them a
suitable error message.
'''

#Solution

message1 = "1) Square" 
message2 = "2) Triangle"
print(message1)
print(message2)

number = int(input("Enter any of the displayed number above: "))

if number == 1:
    side = int(input("What is the length of one of its sides?: "))
    area = side ** 2
    print(f"The area of the square is: {area}")
elif number == 2:
    height = int(input("What is the height?: "))
    base = int(input("What is the base?: "))
    areaa = (height * base ) / 2
    print(f"The area of the triangle is: {areaa}")
else:
    print("Wrong Entry!")
