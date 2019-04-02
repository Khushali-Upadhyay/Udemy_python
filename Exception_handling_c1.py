>>> 10 / 0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    10 / 0
ZeroDivisionError: division by zero
>>> try:
	length = 10
	width = 0
	length / width
except Exception:
	print("Division by zero is invalid!Kindly change your input")

	
Division by zero is invalid!Kindly change your input
>>> del(width)
>>> width
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    width
NameError: name 'width' is not defined
>>> try:
	length / width
except Exception:
	print("Division by zero is invalid!Kindly change your input")

	
Division by zero is invalid!Kindly change your input
>>> try:
	length / width
except NameError:
	print("Variable has been used before defining it.")

	
Variable has been used before defining it.
>>> try:
	length / width
except NameError:
	print("Variable has been used before defining it.")
except ZeroDivisionError:
	print("Division by zero is invalid!Kindly change your input")

	
Variable has been used before defining it.
>>> try:
	width = 0
	length / width
except NameError:
	print("Variable has been used before defining it.")
except ZeroDivisionError:
	print("Division by zero is invalid!Kindly change your input")

	
Division by zero is invalid!Kindly change your input
>>> 
