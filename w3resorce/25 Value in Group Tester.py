#Write a Python program that checks whether a specified value is contained within a group of values.
#Test Data :
#3 -> [1, 5, 8, 3] : True
#-1 -> [1, 5, 8, 3] : False

def tester(test,list):
    for x in list:
        if x==test:
            print("there is a "+str(test))
            break
    else:
        print("there is no "+str(test))

tester(1,[0,5,6,7,4,3])
tester(1,[0,5,7,4,1,0])