#!/usr/bin/env python
# coding: utf-8

# In[4]:


cat = "meow"; dog = "woof" ; parrot = "hello"
print(cat, dog, parrot,sep = ",",end = "!")
print()

meow,woof,hello!


# In[5]:


"THIS IS A 'QUOTE' INSIDE A STRING"

"THIS IS A 'QUOTE' INSIDE A STRING"


# In[9]:


day = "GOOD   DAY"
night = "good night"
len(day)

day.lower()

10
'good   day'


# In[8]:


type(day)

str


# In[11]:


lang = "Python"
"This is a cool " + lang + " course"

'This is a cool Python course'


# In[15]:


num = 20
"lecture " + str(num) + " is on strings"

'lecture 20 is on strings'



# In[18]:


"20" + "50"
type(eval)

type(eval("45.3"))

eval("20") + eval ("50")

eval("20 + 50")


float
70
70


# In[19]:


check = "a a a B b b b c c"
check.count("b")

3

# In[24]:


messy = """"\\PLEASE #@CLEAN UP #@THIS MESSY #@DOCSTRING 
WHICH --CAN HAVE \\MULTIPLE LINES\\
OF STRING--"""
messy.replace("\\", "").replace("#@", "").replace("--", "").replace("\n", "").lower()


'"please clean up this messy docstring which can have multiple linesof string'

# In[ ]:


pet = "cat"


# In[25]:


pet[0]

'c'

