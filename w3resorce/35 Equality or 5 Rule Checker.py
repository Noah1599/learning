#Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

values=input("gimme 2 ints : ").split(",")
a,b=map(int,values)

answer=False

if(a==b or a+b==5 or abs(a-b)==5):
    answer=True

print(answer)