Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print()

>>> print("Hello"*3)
HelloHelloHello
>>> print("All the power is within you")
All the power is within you
>>> print("All the power \n is within you")
All the power 
 is within you
>>> a,b=10,20
>>> print(a,b,sep=',')
10,20
>>> name="John"
>>> marks=94.567
>>> print("Name is", name, "Marks are", marks)
Name is John Marks are 94.567
>>> print("Name is {}, Marks are {}".format(name,marks))
Name is John, Marks are 94.567
>>> print("Name is {0}, Marks are {1}".format(name,marks))
Name is John, Marks are 94.567
>>> s=input()
123
>>> print(s)
123
>>> s1=input("Enter your name:")
Enter your name:Khushali
>>> print(s1)
Khushali
>>> i=int(input("Enter an integer number"))
Enter an integer number12
>>> print(i)
12
>>> print(type(i))
<class 'int'>
>>> list=[int(x) for x in input("Enter three numbers seperated by coma:").split(',')]
Enter three numbers seperated by coma:1,2,3
>>> print(list)
[1, 2, 3]
>>> 
