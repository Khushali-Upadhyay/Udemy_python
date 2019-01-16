Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Easy
>>> def helloWorld():
	print("Hello World!")

	
>>> helloWorld()
Hello World!
>>> # Medium
>>> number1 = 10
>>> number2 = 20
>>> def returnSum(number1, number2):
	sum = number1 + number2
	return sum

>>> returnSum(number1, number2)
30
>>> # Hard
>>> side1 = 5
>>> side2 = 5
>>> side3 = 5
>>> def triangleType(side1, side2, side3):
	if side1 == side2 == side3:
		if side2 == side3:
			return("Equilateral triangle")
		else:
			return("Isosceles traingle")
	elif side2 == side3:
		return("Isosceles traingle")
	else:
		return("Scalene triangle")
	triangle = triangleType(side1, side2, side3)
	print(traingle)

	
>>> traingleType(side1, side2, side3)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    traingleType(side1, side2, side3)
NameError: name 'traingleType' is not defined
>>> triangleType(side1, side2, side3)
'Equilateral triangle'
>>> 
