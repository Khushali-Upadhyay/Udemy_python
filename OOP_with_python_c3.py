Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Creating first class
>>> class Product:
	def __init__(self):     #Its a constructor which has inbuilt method named init for every class and has keyword self which points to current object
		self.name="iPhone"
		self.description="Its awesome!"
		self.price=700

		
>>> p1 = Product()              #We use name of class and parenthesis to define an object
>>> print(p1.name)              #We use objectName. to access object's variables
iPhone
>>> print(p1.description)
Its awesome!
>>> print(p1.price)
700
>>> #Parameterized constructor
>>> class Product:
	def __init__(self,name,ratings):          #Whatever parameters you pass will be stored inside variables
		self.name=name
		self.ratings=ratings

		
>>> c1=Product("Java",[1,2,3,4,5])
>>> print(c1.name)
Java
>>> print(c1.ratings)
[1, 2, 3, 4, 5]
>>> #Instance method
>>> class Course:
	def __init__(self,name,ratings):
		self.name=name
		self.ratings=ratings
	
	def average(self):
		numberOfRatings=len(self.ratings)
		average=sum(self.ratings)/numberOfRatings
		print("Average Ratings for",self.name,"is",average)

		
>>> c1=Course("Java",[1,2,3,4,5])
>>> print(c1.name)
Java
>>> print(c1.ratings)
[1, 2, 3, 4, 5]
>>> c1.average()
Average Ratings for Java is 3.0
>>> #Getter and setter methods
>>> class Programmer:
	def setName(self,n):
		self.name=n
	def getName(self):
		return self.name
	def setSalary(self,sal):
		self.salary=sal
	def getSalary(self):
		return self.salary
	def setTechnologies(self,techs):
		self.technologies=techs
	def getTechnologies(self):
		return self.technologies

>>> p1=Programmer()
>>> p1.setName("John")
>>> p1.setSalary(10000)
>>> p1.setTechnologies(["Java","Python"])
>>> print(p1.getName())
John
>>> print(p1.getSalary())
10000
>>> print(p1.getTechnologies())
['Java', 'Python']
>>> #Instance method
>>> class Product:
	def __init__(self):
		self.name="iPhone"
		self.description="Its awesome"
		self.price=700
	def display(self):
		print(self.name)
		print(self.description)
		print(self.price)

		
>>> p1=Product()
>>> p1.display()
iPhone
Its awesome
700
>>> #Static field
>>> class Student:
	major="SE"
	def __init__(self,name):
		self.name=name

		
>>> s1=Student("John")
>>> print(s1.major)
SE
>>> print(s1.name)
John
>>> print(Student.major)         #To access static variable we can use class name
SE
>>> #Count number of objects
>>> class ObjectCounter:
	numberOfObjects=0
	def __init__(self):
		ObjectCounter.numberOfObjects+=1
	@staticmethod
	def displayCount():
		print(ObjectCounter.numberOfObjects)

		
>>> o1=ObjectCounter()
>>> ObjectCounter.displayCount()
1
>>> #Inner class
>>> class Car:
	def __init__(self,make,year):
		self.make=make
		self.year=year
	class Engine:
		def __init__(self,number):
			self.number=number

			
>>> c=Car("BMW",2018)
>>> e=c.Engine(123)
>>> print(c.make)
BMW
>>> print(c.year)
2018
>>> print(e.number)
123
>>> #Init-Used to create and initialize fields
