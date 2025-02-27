#Write a Python program that determines whether a given number (accepted from the user) is even or odd, 
# and prints an appropriate message to the user.

num=int(input("write a number : "))

def numberCal(number):
    if (number%2)==0:
        print("number is even")
    else:
        print("number is uneven")

numberCal(num)