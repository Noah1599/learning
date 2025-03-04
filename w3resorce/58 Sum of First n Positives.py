#Write a Python program to sum the first n positive integers.
#nums=list(map(int,input("write me a bunch of numbers : ")))
#pos=int(input("How many of the first numbers do you want the sum of : "))
#
#def cal(numbers,amount):
#    sum=int(0)
#    for x in range(amount):
#        sum+=numbers[x]
#    return sum
#
#sum=cal(nums,pos)
#print(sum)

n=int(input("how many firt n positive ints : "))

sum=(n*(n+1))/2
print(sum)