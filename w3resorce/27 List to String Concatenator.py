#Write a Python program that concatenates all elements in a list into a string and returns it.
myList = [42, "hello", 3.14, True, None, [1, 2, 3], {"key": "value"}, (4, 5), {9, 8, 7}, b"bytes"]

myList=" ".join(map(str,myList))

print(myList)
