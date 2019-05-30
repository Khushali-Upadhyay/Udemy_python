Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # 1 2 3
>>> # 4 5 6
>>> # 7 8 9
>>> 
>>> number = 1
>>> for row in range(1,4):
	for column in range(1,4):
		print(number, end = ' ')
		number = number + 1
	print()

	
1 2 3 
4 5 6 
7 8 9 
>>> 
