#Write a Python program to check whether a file exist
import os
print(os.getcwd())
print(os.path.isfile('w3resorce/readme.py'))
print(os.path.isfile('main.py'))

with open('w3resorce/readme.py', 'r') as file:
    content = file.read()
    print(content)