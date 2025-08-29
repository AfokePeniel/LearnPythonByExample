'''
Write a program that will ask for a number of days and then will show how many
hours, minutes and seconds are in that number of days.
'''
# Solution
numb_days = int(input("Kindly enter any number of days: "))


day_hr = 24 * numb_days
min = 60 * day_hr
sec = min * 60

print(numb_days,"days has " + str(day_hr) +" hours, " + str(min),"minutes and" + " " + str(sec), "seconds.")
