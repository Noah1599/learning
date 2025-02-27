#Write a Python program to calculate the sum of three given numbers. 
#If the values are even, return three times their sum.

numbers=input("write 3 numbers seperated by space : ")

nSplit=numbers.split(" ")

sum=int(nSplit[0])+int(nSplit[1])+int(nSplit[2])

if (sum%2)==0:
    print("numbers are even "+str(sum*3))
else:
    print("numbers are uneven "+str(sum))