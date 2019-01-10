Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Easy
>>> message = "Python programming is easy"
>>> print(message)
Python programming is easy
>>> # Medium
>>> slicedText = message[22:26]
>>> print(slicedText)
easy
>>> #Hard
>>> text = slicedText.replace("easy","and powerful")
>>> concatenatedString = message + slicedText
>>> print(concatenatedString)
Python programming is easyeasy
>>> concatenatedString = message + text
>>> print(concatenatedString)
Python programming is easyand powerful
>>> 
