'''
Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the
number of diners and show how much each person must pay.
'''

#Solution

total_bill = int(input("Kindly enter the total bill amount: \n"))
total_diners = int(input("Kindly enter the number of diners: \n"))
each_bill = total_bill / total_diners

print("Each diner will pay: $", each_bill)