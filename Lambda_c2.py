#!/usr/bin/env python
# coding: utf-8

# In[2]:


def add(arg1, arg2):
    return arg1 + arg2

add(10, 20)

30

# In[6]:


g = lambda x, y : x + y
g(10, 20)

30

# In[8]:


g = lambda x = 50, y = 20 : x + y
g()

70

# In[9]:


g = lambda x = 50, y = 20 : x + y
g(10, 30)


40
# In[10]:


def check(num):
    return num % 2 == 0 and num > 8

check(13)

False

# In[12]:


g2 = lambda num: num % 2 == 0 or num > 8
g2(3)

False

# In[ ]:


def compare(a, b):
    if a > 10:
        return a
    else:
        return b
compare(20, 2)

20
# In[13]:


def size(x):
    if x > 100:
        return "big"
    else:
        return "small"
size(1000)

'big'

# In[14]:


g4 = lambda x:"Big" if x > 100 else "small"
g4(1000)

'Big'

# In[ ]:




