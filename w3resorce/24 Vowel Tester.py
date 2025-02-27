#Write a Python program to test whether a passed letter is a vowel or not.

vovels="AEIOU"
test=input("What lettet do you wanna test? : ").upper()
for x in vovels:
    if test==x:
        print("This is a vovel")
        break
else:
    print("This is no vovel")