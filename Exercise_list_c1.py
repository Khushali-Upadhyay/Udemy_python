
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
