Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # break     It stops loop from further execution
>>> for number in range(1,11):
	if number == 5:
		break
	else:
		print(number)

		
1
2
3
4
>>> # continue          To skip a particular iteration
>>> for number in range(1,11):
	if number == 5:
		continue
	else:
		print(number)

		
1
2
3
4
6
7
8
9
10
>>> # else          It checks for break statement, if not then else is executed           
>>> for number in range(1,11):
	if number == 15:
		break
	else:
		print(number)
else:
	print("All the numbers were printed without breaking the loop")

	
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
All the numbers were printed without breaking the loop
>>> for number in range(1,11):
	if number == 5:
		break
	else:
		print(number)
else:
	print("All the numbers were printed without breaking the loop")

	
1
2
3
4

