Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Polymorphism-Different behaviour based on objects that are dealt
>>> #Duck typing
>>> class Human:
	def talk(self):
		print("Hello")

		
>>> class Duck:
	def talk(self):
		print("Quack Quack")

		
>>> def callTalk(obj):
	obj.talk()

	
>>> d=Duck()
>>> callTalk(d)
Quack Quack
>>> h=Human()
>>> callTalk(h)
Hello
>>> #Dependency Injection
>>> class Flight:
	def __init__(self,engine):
		self.engine=engine
	def startEngine(self):
		self.engine.start()

		
>>> class AirbusEngine:
	def start(self):
		print("Starting Airbus engine")

	
>>> class BoingEngine:
	def start(self):
		print("Starting BoingEngine engine")

		
>>> ae=AirbusEngine()
>>> f=Flight(ae)
>>> f.startEngine()
Starting Airbus engine
>>> be=BoingEngine()
>>> f1=Flight(be)
>>> f1.startEngine()
Starting BoingEngine engine
>>> #Operator overloading
>>> x=10
>>> y=20
>>> print(x+y)
30
>>> s1="Hello"
>>> s2="How are you"
>>> print(s1+s2)
HelloHow are you
>>> l1=[1,2,3]
>>> l2=[4,5,6]
>>> print(l1+l2)
[1, 2, 3, 4, 5, 6]
>>> 
