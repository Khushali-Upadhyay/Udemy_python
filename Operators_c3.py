Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a,b=10,5
>>> print('Addition',a+b)
Addition 15
>>> print('Subtraction',a-b)
Subtraction 5
>>> print('Multiplication',a*b)
Multiplication 50
>>> print('Division',a/b)
Division 2.0
>>> print('Modulas',a%b)
Modulas 0
>>> print('Power',a**b)
Power 100000
>>> print('Floor division',a//b)
Floor division 2
>>> x,y=10,5
>>> x+=y
>>> print(x)
15
>>> x*=y
>>> print(x)
75
>>> x,y=77,88
>>> print(x==y)
False
>>> print(x!=y)
True
>>> print(x>y)
False
>>> print(x,y)
77 88
>>> print(x>=y)
False
>>> print(x<y)
True
>>> x=25
>>> y=30
>>> print((x==25 and y==30))
True
>>> print((x=25 and y==31))
SyntaxError: invalid syntax
>>> print((x==25 and y==31))
False
>>> print((x==25 or y==31))
True
>>> print((x==25 or y==31))
True
>>> print((x==26 or y==31))
False
>>> print(not(x==25 or y==31))
False
>>> 
