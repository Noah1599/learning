#Write a Python program that calls an external command.
from subprocess import call

call(["dir"], shell=True)