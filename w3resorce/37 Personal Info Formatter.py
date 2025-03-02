#Write a Python program that displays your name, age, and address on three different lines.
info=input("write you name age and adress : ").split(" ")

name=info[0]
age=info[1]
adress=" ".join(map(str,info[2:]))

print("the information is\n"+name+"\n"+age+"\n"+adress)
print("name: {}\nage: {}\nadress: {}".format(name,age,adress))
