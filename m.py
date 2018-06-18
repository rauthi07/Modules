#Q1
'''A time tuple is the usage of a tuple (list of ordered items/functions) for the ordering and notation of time.
Basically, the tuples for time are just a way of ordering the values for any given specific moment in time.
month (1 to 12),day (1 to 31), hour (0 to 23), minutes (0 to 59), seconds (0 to 59), 
day of the week (0 to 6, where 0 = Monday and 6 = Sunday), day of the year (1 to 366).

#Q2 formatted time
'''import time
print (time.asctime())'''

#Q3&Q4 Extract month&day from the time
'''import datetime
time=datetime.date(2018,6,18)
print(time.month)
print(time.day)'''

#Q5
'''from datetime import date
print(date.today())
print(date.strftime("%a, %b %d, %Y"))'''


#Q6
'''import time
print(time.localtime())'''

#Q7
'''import math
A=int(input('enter a no:'))
print(math.factorial(A))'''

#Q8
'''import math
A=int(input('enter a no:'))
B=int(input('enter a no:'))
print(math.gcd(A,B))'''

#Q9
'''import os
print(os.getcwd())
print(os.environ['HOME'])'''

