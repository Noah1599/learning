#Write a Python program to count the number 4 in a given list.

numbers=input("write a bunch of numbers : ")
count=0
for x in numbers:
    if x==str(4):
        count=count+1

print("there are "+str(count)+" times 4 in the list")