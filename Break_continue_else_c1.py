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
>>> 
