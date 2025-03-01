#Write a Python program to find the least common multiple (LCM) of two positive integers.

import math

def LCM(a,b):
    gcd=math.gcd(a,b)
    lcm=abs(a*b)//gcd
    return lcm

num1=36
num2=60


least=LCM(num1,num2)
print(least)