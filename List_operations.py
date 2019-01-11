Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> favouriteFruits = ["Apple", "Orange", "Strawberry"]
>>> favouriteFruits
['Apple', 'Orange', 'Strawberry']
>>> # list.append()                   # Appends an element at the last position
>>> favouriteFruits.append("Kiwi")
>>> favouriteFruits
['Apple', 'Orange', 'Strawberry', 'Kiwi']
>>> # list.insert()                   # Inserts element at the respective index
>>> favouriteFruits.insert(1, "Mango")
>>> favouriteFruits
['Apple', 'Mango', 'Orange', 'Strawberry', 'Kiwi']
>>> # list.remove()                   # Removes the element from the list
>>> favouriteFruits.remove("Strawberry")
>>> favouriteFruits
['Apple', 'Mango', 'Orange', 'Kiwi']
>>> # list.sort()                     # Sorts elements in alphabetical order
>>> favouriteFruits.sort()
>>> favouriteFruits
['Apple', 'Kiwi', 'Mango', 'Orange']
>>> # list.reverse()                  # Reverses the order in the list
>>> favouriteFruits.reverse()
>>> favouriteFruits
['Orange', 'Mango', 'Kiwi', 'Apple']
>>> # list.pop()                      # Removes the last element 
>>> favouriteFruits.pop()               
'Apple'
>>> 
