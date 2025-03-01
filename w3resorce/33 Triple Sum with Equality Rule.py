#Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
valueList=input("write three int seperated by . : ").split(",")

a,b,c=map(int,valueList)

value=a+b+c

if(a==b or a==c or b==c):
    value=0
print(value)

#value=sum(int(x) for x in valueList)