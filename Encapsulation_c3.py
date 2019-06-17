Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Private fields and name mangling
>>> class Student:
	def __init__(self):
		self.__id=123          #__ is used to define private variables
		self.__name="John"
	def display(self):
		print(self.__id)
		print(self.__name)

		
>>> s=Student()
>>> s.display()
123
John
>>> print(s._Student__id)
123
>>> print9s._Student__name)
SyntaxError: invalid syntax
>>> print(s._Student__name)
John
>>> #Implementing encapsulation
>>> class Student:
	def setId(self,id):
		self.id=id
	def getId(self):
		return self.id
	def setName(self,name):
		self.name=name
	def getName(self):
		return self.name

	
>>> s=Student()
>>> s.setId=123
>>> s.setName("John")
>>> print(s.getId())
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(s.getId())
  File "<pyshell#24>", line 5, in getId
    return self.id
AttributeError: 'Student' object has no attribute 'id'
>>> print(s.getName())
John
>>> 
