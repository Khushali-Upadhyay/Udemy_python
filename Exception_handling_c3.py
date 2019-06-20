Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Exceptions are runtime errors.BaseException is the base class and Exception inherits it.Exception is inherited by Standard Error and Warning.Errors include EOF,ZeroDivision and Indentation.Warnings include Deprecated warning which occurs when you use outdated packages and import warning occurs when you import something and dont use it.
>>> #Handling exceptions
>>> try:
	a,b=[int(x) for x in input("Enter two numbers:").split()]
	c=a/b
	print(c)
except ZeroDivisionError:
	print("Division by zero is not allowed")
	print("Please enter a non zero number")
	print("Code after the exception")

	
Enter two numbers:4 2
2.0
>>> 
>>> #Finally
>>> try:
	f=open("File1","w")
	a,b=[int(x) for x in input("Enter two numbers:").split()]
	c=a/b
	print(c)
	f.write("Writing %d into file" %c)
except ZeroDivisionError:
	print("Division by zero is not allowed")
	print("Please enter a non zero number")
finally:
	f.close()
	print("File closed")
	print("Code after the exception")

	
Enter two numbers:4 0
Division by zero is not allowed
Please enter a non zero number
File closed
Code after the exception
>>> #Else
>>> try:
	f=open("File1","w")
	a,b=[int(x) for x in input("Enter two numbers:").split()]
	c=a/b
	print(c)
	f.write("Writing %d into file" %c)
except ZeroDivisionError:
	print("Division by zero is not allowed")
	print("Please enter a non zero number")
else:
	print("You have entered a non zero number")
finally:
	f.close()
	print("File closed")
	print("Code after the exception")

	
Enter two numbers:4 2
2.0
19
You have entered a non zero number
File closed
Code after the exception
>>> #Logging in action
>>> import logging
>>> logging.error("Error")
ERROR:root:Error
>>> logging.critical("Critical")
CRITICAL:root:Critical
>>> logging.warning("Warning")
WARNING:root:Warning
>>> logging.debug("Debug")
>>> logging.info("Info")
>>> #Logging configuration
>>> import logging
>>> logging.basicConfig(filename="mylog.log",level=logging.ERROR)
>>> logging.critical("Critical")
CRITICAL:root:Critical
>>> logging.error("Error")
ERROR:root:Error
>>> logging.warning("Warning")
WARNING:root:Warning
>>> logging.info("Info")
>>> logging.debug("Debug")
>>> #Log exceptions
>>> import logging
>>> logging.basicConfig(filename="mylog.log",level=logging.DEBUG)
>>> try:
	f=open("myfile","w")
	a,b=[int(x) for x in input("Enter two numbers:").split()]
	logging.info("Division in progress")
	c=a/b
	f.write("Writing %d into file" %c)
except ZeroDivisionError:
	print("Division by zero is not allowed")
	print("Please enter a non zero number")
	logging.error("Division by zero")
else:
	print("You have entered a non zero number")
finally:
	f.close()
	print("File closed")
	print("Code after the exception")


Enter two numbers:5 0
Division by zero is not allowed
Please enter a non zero number
ERROR:root:Division by zero
File closed
Code after the exception
>>> #Assertion
>>> try:
	num=int(input("Enter an even number"))
	assert num%2==0,"You have entered an invalid input or an odd number"
except AssertionError as obj:
	print(obj)
print("After assertion")
SyntaxError: invalid syntax
>>> try:
	num=int(input("Enter an even number"))
	assert num%2==0,"You have entered an invalid input or an odd number"
except AssertionError as obj:
	print(obj)
	print("After assertion")

	
Enter an even number9
You have entered an invalid input or an odd number
After assertion
>>> 
