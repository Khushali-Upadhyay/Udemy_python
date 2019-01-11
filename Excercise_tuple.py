Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Easy
>>> dateOfBirth = ("04-02-1781","10-03-1995","11-15-1985","07-09-2016")
>>> dateOfBirth
('04-02-1781', '10-03-1995', '11-15-1985', '07-09-2016')
>>> dateOfBirth = list(dateOfBirth)
>>> 
=============================== RESTART: Shell ===============================
>>> # Easy
>>> dateOfBirth = ("04-02-1781","10-03-1995","11-15-1985","07-09-2016")
>>> dateOfBirth
('04-02-1781', '10-03-1995', '11-15-1985', '07-09-2016')
>>> # Medium
>>> dateOfBirth = list(dateOfBirth)
>>> dateOfBirth
['04-02-1781', '10-03-1995', '11-15-1985', '07-09-2016']
>>> # Hard
>>> dateOfBirth.remove("04-02-1781")
>>> dateOfBirth
['10-03-1995', '11-15-1985', '07-09-2016']
>>> dateOfBirth = type(dateOfBirth)
>>> dateOfBirth
<class 'list'>
>>> dateOfBirth = tuple(dateOfBirth)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    dateOfBirth = tuple(dateOfBirth)
TypeError: 'type' object is not iterable
>>> print(dateOfBirth)
<class 'list'>
>>> newDateOfBirth = tuple(dateOfBirth)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    newDateOfBirth = tuple(dateOfBirth)
TypeError: 'type' object is not iterable
>>> 
