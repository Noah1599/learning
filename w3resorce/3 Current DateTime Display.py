#Write a Python program to display the current date and time.

import datetime

now=datetime.datetime.now()

print(now.strftime("%Y-%m-%d %H:%M:%S"))

#%Y is year and so on