Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Regular expression is used to search a substring within a given string or validate the given string such as email or password.
>>> # Match \d-digit,\D-non digit,\s-white space,\S-non white space,\w=alphanumeric,\W-non alphanumeric,\b-space between words,\A-start of string,\Z-end of string.
>>> #Search
>>> import re
>>> str="Take up one idea.One idea at a time"
>>> result=re.search(r'o\w\w',str)
>>> print(result.group())
one
>>> #Findall and match
>>> import re
>>> str="Take up one idea, one idea at a time"
>>> result=re.findall(r'o\w\w',str)
>>> print(result)
['one', 'one']
>>> import re
>>> str="Take up one idea, one idea at a time"
>>> result=re.match(r'T\w\w',str)
>>> print(result.group())
Tak
>>> #Match matches the starting of the string and returns the result
>>> #Split
>>> import re
>>> str="Take 1 up one 23 idea, one idea 45 at a time"
>>> result=re.split(r'\d+',str)
>>> print(result)
['Take ', ' up one ', ' idea, one idea ', ' at a time']
>>> #Substitute
>>> import re
>>> str="Take up one idea, one idea at a time"
>>> result=re.sub(r'One','Two',str)
>>> print(result)
Take up one idea, one idea at a time
>>> import re
>>> str="Take up One idea, One idea at a time"
>>> result=re.sub(r'One','Two',str)
>>> print(result)
Take up Two idea, Two idea at a time
>>> #Quantifiers + means one or more repetition,* means 0 or more repetition,? means 0 or 1 repetition,m means exactly m occurences and {m,n} means minimum m and maximum n.
>>> #Quantifiers
>>> import re
>>> str="Take up One idea, One idea at a time"
>>> result=re.findall(r'O\w+',str)
>>> print(result)
['One', 'One']
>>> #Matching dates
>>> import re
>>> str="Take up 22-06-2019 One idea, One idea at a time 24-06-2019"
>>> result=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
>>> print(result)
['22-06-2019', '24-06-2019']
>>> # \-escape character, .-matches any character except a new line,^-match beginning of a string,$-match end of string,[...]-range matching,[^...]-matches character except that in the range,(...)-match regular expression inside parenthesis,(R|S)-matches either of R or S.
>>> #Special symbols
>>> import re
>>> str="Take up One idea, One idea at a time"
>>> result=re.search(r'T\w*',str)
>>>  print(result.group())
Take
>>> 
