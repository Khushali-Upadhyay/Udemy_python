Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # tupleName = (object1, object2, object3)
>>> # Tuple to store start dates of World War I and II
>>> historicDates = (1914, 1939)
>>> historicDates[0]
1914
>>> historicDates[1] = 2017           # Since its immutable it cannot be changed
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    historicDates[1] = 2017
TypeError: 'tuple' object does not support item assignment
>>> del(historicDates)                # Deleting tuple
>>> historicDates
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    historicDates
NameError: name 'historicDates' is not defined
>>> 
