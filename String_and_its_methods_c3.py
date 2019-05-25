Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s="You are awesome"
>>> print(s)
You are awesome
>>> s1="""You are
the creator
of your own destiny"""
>>> print(s1)
You are
the creator
of your own destiny
>>> print(s[2])
u
>>> print(s*3)
You are awesomeYou are awesomeYou are awesome
>>> print(len(s))
15
>>> print(len(s1))
39
>>> print(s[0:5])
You a
>>> print(s[0:])
You are awesome
>>> print(s[:0])

>>> print(s[:8])
You are 
>>> print(s[-3:-1])
om
>>> print(s[0:9:2])
Yuaea
>>> print(s[::-1])
emosewa era uoY
>>> print(s.strip())
You are awesome
>>> print(s.lstrip())
You are awesome
>>> print(s.rstrip())
You are awesome
>>> print(s.find("awe",0,8))
-1
>>> print(s.count("a"))
2
>>> print(s.replace('awesome','super'))
You are super
>>> print(s.upper())
YOU ARE AWESOME
>>> print(s.lower())
you are awesome
>>> print(s.title())
You Are Awesome
>>> 
