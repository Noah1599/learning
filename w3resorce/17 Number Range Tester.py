#Write a Python program to test whether a number is within 100 of 1000 or 2000.

inputNum=int(input("Write a number you want to test is between 100 and 1000 or 2000 : "))

if inputNum>=100 and inputNum<1000:
    print("number is between 100 and 1000")
elif inputNum>=1000 and inputNum<=2000:
    print("number is between 1000 and 2000")
else:
    print("out of scope")