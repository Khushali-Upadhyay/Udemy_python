Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Student details
>>> studentid = int(input("Enter Student ID:"))
Enter Student ID:1
>>> name = input("Enter student name:")
Enter student name:Avi
>>> marks = float(input("Enter student marks:"))
Enter student marks:95.06
>>> print("Student ID is", studentid, "Student name is", name, "Student marks is", marks)
Student ID is 1 Student name is Avi Student marks is 95.06
>>> #Average of 3 numbers
>>> a,b,c = [int(x) for x in input("Enter 3 numbers:").split()]
Enter 3 numbers:5 10 15
>>> average = (a+b+c)/3
>>> print("Average is:",average)
Average is: 10.0
>>> #Area of circle
>>> r = float(input("Enter radius:"))
Enter radius:3
>>> pi=22/7
>>> area=pi*r**2
>>> print(area)
28.285714285714285
>>> #Above program using math module
>>> import math
>>> r = float(input("Enter radius:"))
Enter radius:5
>>> area=math.pi*r**2
>>> print(area)
78.53981633974483
>>> #Function as parameter to another function
>>> def display(function):
	return "Hello " + function

>>> def name():
	return "John"

>>> print(display(name()))
Hello John
>>> 
