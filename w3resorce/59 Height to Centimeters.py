#convert feet and inches to cm
choice=int(input("1 is feet to cm \n2 is cm to feet : "))
height=input("write your hight in feet and inches : ").split(" ")

x=30.48
y=2.54
feet=0
if choice==1:
    cmHeight=int(height[0])*x+int(height[1])*y
    print(cmHeight)
else:
    inchheight=int(height[0])/y
    while inchheight>=12:
        inchheight-=12
        feet+=1
    print(feet,inchheight)



