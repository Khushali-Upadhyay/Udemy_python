Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Easy
>>> colours = ["Pink","Purple","Red","Blue","Orange"]
>>> colours
['Pink', 'Purple', 'Red', 'Blue', 'Orange']
>>> # Medium
>>> colours[2] = "Yellow"
>>> colours
['Pink', 'Purple', 'Yellow', 'Blue', 'Orange']
>>> # Hard
>>> moreColours = ["Red","Green","Brown"]
>>> moreColours
['Red', 'Green', 'Brown']
>>> finalColours[] = colours[] + moreColours[]
SyntaxError: invalid syntax
>>> finalColours = colours + moreColours
>>> finalColours
['Pink', 'Purple', 'Yellow', 'Blue', 'Orange', 'Red', 'Green', 'Brown']
>>> 
