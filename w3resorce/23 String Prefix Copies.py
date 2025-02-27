#Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
# Return n copies of the whole string if the length is less than 2.
n=4
string=input("write string : ")
firstTwo=string[0:2]

print(firstTwo*n)
