#Write a Python program to add two objects if both objects are integers.

obj1=int(3)
obj2=int(2)
obj3=float(4)
obj4=float(5)


def addIfInt(a,b):
    if type(a)==type(b) and type(a)==int:
        print(a+b)
    else:
        print("failed")

addIfInt(obj1,obj2)
addIfInt(obj3,obj2)
addIfInt(obj3,obj4)