Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>#Epoch
>>> import time
>>> epochseconds=time.time()
>>> print(epochseconds)
1561054440.1492898
>>> t=time.ctime(epochseconds)
>>> print(t)
Thu Jun 20 11:14:00 2019
>>> #Current date and time
>>> import time,datetime
>>> epochseconds=time.time()
>>> print(epochseconds)
1561055436.6791995
>>> t=time.ctime(epochseconds)
>>> print(t)
Thu Jun 20 11:30:36 2019
>>> dt=datetime.datetime.today()
>>> print("Current Date:{}/{}/{}".format(dt.day,dt.month,dt.year))
Current Date:20/6/2019
>>> print("Current Time:{}:{}:{}".format(dt.hour,dt.minute,dt.second))
Current Time:11:34:21
>>> #Combining date and time
>>> from datetime import*
>>> d=date(2018,7,21)
>>> t=time(12,45)
>>> dt=datetime.combine(d,t)
>>> print(dt)
2018-07-21 12:45:00
>>> #Sorting dates
>>> from datetime import*
>>> ldates =[]
>>> d1=date(2016,8,12)
>>> d2=date(2018,7,12)
>>> d3=date(2017,6,12)
>>> ldates.append(d1)
>>> ldates.append(d2)
>>> ldates.append(d3)
>>> ldates.sort()
>>> for d in ldates:
	print(d)

	
2016-08-12
2017-06-12
2018-07-12
>>> #Sleep()
>>> from datetime import date
>>> import time
>>> ldates=[]
>>> d1=date(2016,8,12)
>>> d2=date(2018,7,12)
>>> d3=date(2017,6,12)
>>> ldates.append(d1)
>>> 
KeyboardInterrupt
>>> ldates.append(d2)
>>> ldates.append(d3)
>>> ldates.sort()
>>> time.sleep(3)
>>> for d in ldates:
	print(d)

	
2016-08-12
2017-06-12
2018-07-12
>>> #Execution time of a program
>>> from datetime import date
>>> import time
>>> startTime=time.perf_counter()
>>> ldates=dates[]
SyntaxError: invalid syntax
>>> ldates=[]
>>> d1=date(2016,8,12)
>>> d2=date(2018,7,12)
>>> d3=date(2017,6,12)
>>> ldates.append(d1)
>>> ldates.append(d2)
>>> ldates.append(d3)
>>> ldates.sort()
>>> time.sleep(3)
>>> for d in ldates:
	print(d)

2016-08-12
>>> 
>>> 
>>> endTime=time.perf_counter()
>>> print("Execution Time",endTime-startTime)
Execution Time 198.49638084300022
>>> 
