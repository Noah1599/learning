#Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
#Test Data : amt = 10000, int = 3.5, years = 7
#Expected Output : 12722.79

values=input("write your amount rate and number of years : ").split(",")

amt,intr,year=float(values[0]),float(values[1])/100,float(values[2])

total=amt*(1+intr)**year

print(round(total))