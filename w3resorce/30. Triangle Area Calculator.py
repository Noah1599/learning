#Write a Python program that will accept the base and height of a triangle and compute its area.

heightBase=input("write the height and base lengths : ").split(" ")

height=float(heightBase[0])
base=float(heightBase[1])
area=(height*base)/2
print("the area of the triangle is "+str(round(area)))
