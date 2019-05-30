Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # area = length * width
>>> length = 8
>>> width = 3
>>> area = length * width
>>> area
24
>>> length2 = 10
>>> width2 = 4
>>> area2 = length2 * width2
>>> area2
40
>>> def computeArea(length, width):
	area = length * width
	print(area)

>>> computeArea(length,width)
24
>>> computeArea(length2,width2)
40
>>> def computeArea(length,width):
	area = length * width
	return area

>>> area = computeArea(length,width)
>>> area
24
>>> area2 = computeArea(length2,width2)
>>> area2
40
