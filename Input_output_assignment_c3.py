Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #To check whether given number is a prime number or not
>>> n = int(input("Enter any number:"))
Enter any number:6
>>> for i in range(2,n):
	if (n % i) == 0:
		print("The number is not a prime number")
		break
	else:
		print("The number is a prime number")
		break

	
The number is not a prime number
>>> 
