#Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
import math

p1=(3,11)
p2=(2,43)

dist=math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

print(dist)