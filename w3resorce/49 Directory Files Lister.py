#Write a Python program to list all files in a directory
from os import listdir #listdir gives all files and dir in the current dir
from os.path import isfile, join # isfile makes sure it is a file not a dir

#listdir('w3resorce/') gives a list of all entries dir and files
#isfile(join('w3resorce/',f) checks that the path is a coresponds to file not dir gives true if f is file
#if isfile(join('w3resorce/',f)) makes sure only files go into list
filelist=[f for f in listdir('w3resorce/') if isfile(join('w3resorce/',f))] #this is called a list comprehension

for x in range(len(filelist)):
    print(filelist[x])
