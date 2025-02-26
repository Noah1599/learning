#Write a Python program that calculates the area of a circle based on the radius entered by the user.
import math
radi = float(input("enter the diamiter of you circle."))
area=math.pi*radi**2
print("the area is " + str(area))