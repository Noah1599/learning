#Write a Python program to locate Python site packages.
import site

sitePakages=site.getsitepackages()
print("this is where site packages are located")
for directory in sitePakages:
    print(directory)