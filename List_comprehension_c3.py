Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #List comprehension helps to create one list out of other with easy syntax by applying conditions and logic.
>>>#Cube of numbers in list
>>> list=[]
>>> list=[x**3 for x in range(1,11)]
>>> print(list)
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> #Even numbers between 1 to 20
>>> list=[x for x in range(1,21) if x%2==0]
>>> print(list)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> #Product of numbers in list
>>> a=[1,2,3,4,5]
>>> b=[6,7,8,9,10]
>>> z=[a[i]*b[i] for i in range(len(a))]
>>> print(z)
[6, 14, 24, 36, 50]
>>> #Common elements in the list
>>> a=[2,4,6,8]
>>> b=[1,2,3,4]
>>> result=[i for i in a if i in b]
>>> print(result)
[2, 4]
>>> 
