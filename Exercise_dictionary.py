Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Easy
>>> colourOfVegetables = {"Okra":"Green","Eggplant":"Purple","Potato":"Brown","Carrot":"Orange","Lemon":"Yellow"}
>>> colourOfVegetables
{'Okra': 'Green', 'Eggplant': 'Purple', 'Potato': 'Brown', 'Carrot': 'Orange', 'Lemon': 'Yellow'}
>>> # Medium
>>> colourOfVegetables["Chilli"]="Red"
>>> colourOfVegetables
{'Okra': 'Green', 'Eggplant': 'Purple', 'Potato': 'Brown', 'Carrot': 'Orange', 'Lemon': 'Yellow', 'Chilli': 'Red'}
>>> # Hard
>>> colourOfVegetablesCopy = colourOfVegetables.copy()
>>> colourOfVegetablesCopy
{'Okra': 'Green', 'Eggplant': 'Purple', 'Potato': 'Brown', 'Carrot': 'Orange', 'Lemon': 'Yellow', 'Chilli': 'Red'}
>>> colourOfVegetables.clear()
>>> colourOfVegetables
{}
>>> 
