Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # stringName = "string" or 'string'
>>> fruit = "Apple"
>>> fruit
'Apple'
>>> fruit[0]
'A'
>>> fruit[4]
'e'
>>> fruit[5]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    fruit[5]
IndexError: string index out of range
>>> fruit[-1]               # Prints characters from reverse
'e'
>>> fruit[-2]
'l'
>>> string = 'String is one among Python's data types
SyntaxError: invalid syntax
>>> string = "String is one among Python's data types"     # Declare string under double quotes to avoid error
>>> string
"String is one among Python's data types"
>>> string = 'String is one among Python\'s data types'    # Use escape character which will not treat the character after it as a special character 
>>> string
"String is one among Python's data types"
>>> print("Python is a great programming language for beginners")
Python is a great programming language for beginners
>>> programmingLanguage = "Python"
>>> programmingLanguage
'Python'
>>> print("programmingLanguage is a great programming language for beginners")
programmingLanguage is a great programming language for beginners
>>> print("{} is a great programming language for beginners".format(programmingLanguage)))
SyntaxError: invalid syntax
>>> print("{} is a great programming language for beginners". format(programmingLanguage))
Python is a great programming language for beginners
>>> fruit
'Apple'
>>> fruit = 'Mango'
>>> 
