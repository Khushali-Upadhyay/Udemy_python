Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Abstract class has atleast one abstract method.It will not implement in parent class but child class has to implement it.Also known as interface.If a child class doesnt implement abstract method then it is called abstract class.
>>> from abc import abstractmethod,ABC
>>> class BMW(ABC):
	@abstractmethod
	def drive(self):
		pass

	
>>> class ThreeSeries(BMW):
	def drive(self):
		print("Three series is being driven")

		
>>> class FiveSeries(BMW):
	def drive(self):
		print("Five series is being driven")

		
>>> #Interface-It has all abstract methods
>>> from abc import abstractmethod,ABC
>>> class BMW(ABC):
	@abstractmethod
	def start(self):
		pass
	@abstractmethod
	def stop(self):
		pass
	@abstractmethod
	def drive(self):
		pass

	
>>> class ThreeSeries(BMW):
	def start(self):
		super().start()
		print("Button start")
	def stop(self):
		super().stop()
		print("Button stop")
	def drive(self):
		print("Three series is being driven")

		
>>> class FiveSeries(BMW):
	def start(self):
		super().start()
		print("Button start")
	def stop(self):
		super().stop()
		print("Button stop")
	def drive(self):
		print("Five series is being driven")
