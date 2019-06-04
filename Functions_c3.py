Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #First function
>>> def average(a,b):
	print("Average is: ",(a+b)/2)

	
>>> average(10,20)
Average is:  15.0
>>> #Return usage
>>> def average(a,b):
	return (a+b)/2

>>> result=average(10,20)
>>> print(result)
15.0
>>> #Return multiple values
>>> def calc(a,b):
	x=a+b
	y=a-b
	z=a*b
	w=a/b
	return x,y,z,w

>>> result = calc(10,5)
>>> print(result)
(15, 5, 50, 2.0)
>>> #Global and local variables
>>> x=123
>>> def display():
	y=678
	print(y)

	
>>> print(x)
123
>>> display()
678
>>> #Accessing global variables with the same name
>>> x=123
>>> def display():
	x=678
	print(x)
	print(globals()['x'])

	
>>> print(x)
123
>>> display()
678
123
>>> #Assigning a function to variable
>>> x=123
>>> def display():
	x=678
	print(x)
	print(globals()['x'])

	
>>> print(x)
123
>>> z=display
>>> z()
678
123
>>> #function inside another function
>>> def display():
	def message():
		return "Hello"
	return message

>>> function=display()
>>> print(function())
Hello
>>> #Pass any type
>>> def function(list):
	for i in list:
		print(i)

		
>>> function([1,2,3,4])
1
2
3
4
>>> #Recursion-Use when the same logic is repeating
>>> def factorial(n):
	if n=0:
		
SyntaxError: invalid syntax
>>> def factorial(n):
	if n==0:
		result=1
	else:
		result=n*factorial(n-1)
	return result

>>> print(factorial(5))
120
>>> #Keyword arguments
>>> def average(a,b):
	print(a)
	print(b)
	return (a+b)/2

>>> print(average(b=10,a=20))
20
10
15.0
>>> #Default arguments
>>> def average(a=10,b=20):
	print(a)
	print(b)
	return (a+b)/2

>>> print(average())
10
20
15.0
>>> 
