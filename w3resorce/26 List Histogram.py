#Write a Python program to create a histogram from a given list of integers.
printChar="*"
histogram=input("write your histogram : ")

#histogram=list(map(int,histogram.strip("[]").split(",")))#if u want not write a list but just numbers comment this out

def histoMaker(histo,char):
    for x in histo:
        print(char*int(x))

histoMaker(histogram,printChar)