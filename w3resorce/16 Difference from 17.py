#Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17,
#return twice the absolute difference.

contNum=17

def diffrence(input):
    if contNum<input:
        print("the number is over 17 so restult is "+str((input-contNum)*2))
    else:
        print("the sumber is below 17 so reasult is "+str(contNum-input))

inputNum=int(input("write the number you want to find the diffrence from 17\n"))

diffrence(inputNum)

