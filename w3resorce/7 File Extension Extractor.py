#Write a Python program that accepts a filename from the user and prints the extension of the file.
import string
file=input("what is you file named?:  ")

fileType=file.lstrip(string.ascii_letters)
print(fileType)