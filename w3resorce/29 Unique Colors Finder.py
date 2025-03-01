#Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
#Test Data :
#color_list_1 = set(["White", "Black", "Red"])
#color_list_2 = set(["Red", "Green"])
#Expected Output :
#{'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

def colorfunc(color1,color2):
    #common=color1 & color2 finds the same
    #color1.difference_update(common)
    color1=color1-color2
    print(color1)

colorfunc(color_list_1,color_list_2)