#Write a Python program to calculate the hypotenuse of a right angled triangle.
import math
def triCal(a,b):
    hyp=math.sqrt(a**2+b**2)
    print(hyp)

triCal(2,5)
triCal(12,5)
triCal(7,23)