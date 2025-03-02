#Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
import struct

def check_python_mode():
    mode = struct.calcsize("P") * 8
    print(f"Python is running in {mode}-bit mode.")

check_python_mode()