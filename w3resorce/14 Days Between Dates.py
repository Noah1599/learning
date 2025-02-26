#Write a Python program to calculate the number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)
#Expected output : 9 days
from datetime import datetime

sampleDate=[[2014,7,2],[2014,7,11]]
diffrence=datetime(*sampleDate[1])-datetime(*sampleDate[0])


#the * is used in line 7 to unpack the tuple into datetime
# 
# #print(str(diffrence.days)+"    "+str(sampleDate[1][1]))