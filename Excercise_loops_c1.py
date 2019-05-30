Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Easy
>>> number = 1
>>> for number in range(1,11):
	print(number)

	
1
2
3
4
5
6
7
8
9
10
>>> # Medium
>>> oddSum = 0
>>> for number in range(1,11):
	if number % 2 is not 0:
		oddSum = oddSum + number
	print(oddSum)

	
1
1
4
4
9
9
16
16
25
25
>>> 
=============================== RESTART: Shell ===============================
>>> # Medium
>>> oddSum = 0
>>> for number in range(1,11):
	if number % 2 is not 0:
		oddSum = oddSum + number
     print(oddSum)
     
SyntaxError: unindent does not match any outer indentation level
>>> # Hard
>>> isPrimeNumber = 13
>>> for number in range(2, isPrimeNumber):
	if isPrimeNumber % number is 0:
		print("Number is not a prime number")
	else:
		print("Number is a prime number")

		
Number is a prime number
Number is a prime number
Number is a prime number
Number is a prime number
Number is a prime number
Number is a prime number
Number is a prime number
Number is a prime number
Number is a prime number
Number is a prime number
Number is a prime number
>>> 
