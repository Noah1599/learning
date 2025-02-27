#Write a Python program to get a newly-generated string from a given string 
# where "Is" has been added to the front. 
# Return the string unchanged if the given string already begins with "Is".

sentence=input("write your string : ")

if sentence[0]=="I" and sentence[1]=="s":
    print(sentence)
else:
    