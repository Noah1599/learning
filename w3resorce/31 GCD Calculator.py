#Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
import math

def GCD(a,b):
    gcd=math.gcd(a,b)
    return gcd

num1=36
num2=60


greatest=GCD(num1,num2)
print(greatest)