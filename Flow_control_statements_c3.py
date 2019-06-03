Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Transfer statement tranfers the control of our program from one place to another.Break, continue, pass and return
>>> #Check whether number is odd or even
>>> x=int(input("Enter any number:"))
Enter any number:4
>>> if (x % 2 == 0):
	print(x, "is even")
else:
	print(x, "is odd")

	
4 is even
>>> #If else ladder
>>> x=int(input("Enter any number:"))
Enter any number:0
>>> if x ==0:
	print(x, "is zero")
elif x % 2 == 0:
	print(x, "is even")
else:
	print(x, "is odd")

	
0 is zero
>>> #While loop
>>> y=1
>>> while(y<=20):
	print(y)
	y+=1

	
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
11
12
13
14
15
16
17
18
19
20
>>> #Odd numbers between given numbers
>>> x=int(input("Enter minimum number: "))
Enter minimum number: 1
>>> y=int(input("Enter maximum number: "))
Enter maximum number: 10
>>> i=x
>>> if i % 2 == 0:i=x+1

>>> while i<=y:
	print(i)
	i+=2

	
1
3
5
7
9
>>> #For loop
>>> for x in range(50,71):
	print(x)

50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
>>> #Product of a list
>>> list=[1,2,3,4,5]
>>> product=1
>>> for i in list:
	product*=i
	print("Product is: ", product)

	
Product is:  1
Product is:  2
Product is:  6
Product is:  24
Product is:  120
>>> #Multiplication table
>>> x=int(input("Enter a number for multiplication table:"))
Enter a number for multiplication table:5
>>> for i in range(1,11):
	print(x,"X",i,"=",i*x)

	
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
>>> #Break
>>> list=[3,6,9,5,12]
>>> for i in list:
	if(i==5):
		break
	print(i)

	
3
6
9
>>> #Continue
>>> x=0
>>> while x<20:
	x+=1
	if x%3 == 0:
		continue
	print(x)

	
1
2
4
5
7
8
10
11
13
14
16
17
19
20
>>> #Assert
>>> x=int(input("Enter a number greater than 10"))
Enter a number greater than 1011
>>> assert x>10, "Wrong number entered"
>>> print("You entered", x)
You entered 11
>>> 
