#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
#Sample data : 3, 5, 7, 23

sample="3, 5, 7, 23"
sampleStrip=sample.replace(" ","")

sampleSplit=sampleStrip.split(",")

sampleTuple=tuple(sampleSplit)

print(sampleSplit,"       ",sampleTuple)