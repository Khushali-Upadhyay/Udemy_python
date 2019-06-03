Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> m = int(input("Enter math mark: "))
Enter math mark: 90
>>> p = int(input("Enter physics mark: "))
Enter physics mark: 92
>>> c = int(input("Enter chemistry mark: "))
Enter chemistry mark: 94
>>> avarage = (m+p+c)/3
>>> if (m>=35 and p>=35 and c>=35):
	print("Congratulations...you have passed in exam")
	if (avarage<=59):
		print("Your grade is C...")
	elif (avarage<=69):
		print("Your grade is B...")
	else:
		print("Your grade is A...")
else:
	print("Sorry...you have failed in exam")

	
Congratulations...you have passed in exam
Your grade is A...
>>> 
