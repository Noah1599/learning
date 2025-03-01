#Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

a,b=input("gime 2 numbers, ").split(",")
sum=int(a)+int(b)
if(sum>=15 and sum<=20):
    sum=20
print("this is the returned sum "+str(sum))