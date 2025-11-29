'''
Ask the user to enter their favourite colour. If they enter “red”, “RED” or
“Red” display the message “I like red too”, otherwise display the message
“I don’t like [colour], I prefer red”.
'''

#Solution
colour = input("Enter your favourite colour: ")
if colour == "red" or  colour == "RED" or colour == "Red":
     print("I like red too")
else:
     print(f"I dont like {colour}, i prefer red")
    

   