#Write a Python program that prints the calendar for a given month and year.
#Note : Use 'calendar' module.

import calendar

ym=input("what year do you want the calender and mounth : ")

ymSplit=ym.split(" ")
y=int(ymSplit[0])
m=int(ymSplit[1])

print(calendar.month(y,m))