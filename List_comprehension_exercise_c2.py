#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Convert for loop to list comprehension


# In[2]:


simple = []
for i in range(10):
    s = i + 30
    simple.append(s)
simple



# In[4]:


[i+30 for i in range(10)]

[30, 31, 32, 33, 34, 35, 36, 37, 38, 39]

# In[ ]:


# Convert while loop into list comprehension


# In[5]:


x = 0
case = []
while x < 10:
    s = "The number is " + str(x)
    case.append(s)
    x += 2
case


# In[6]:


[" The number is " + str(x) for x in range(0, 10, 2)]

[' The number is 0',
 ' The number is 2',
 ' The number is 4',
 ' The number is 6',
 ' The number is 8']

# In[ ]:


# Control flow with with modulus in list comprehension


# In[7]:


[d**3 for d in range(20) if d > 10 and d % 2 == 0]

[1728, 2744, 4096, 5832]


# In[ ]:


# Create two nested list comprehension inside the dictionary


# In[13]:


d2  = {"k1": [g + 20 * g for g in range(10) if g < 5],
      "k2": [e * e for e in range(20) if e < 10]}
d3 = {"k3": sum(d2["k1"]) + sum(d2["k2"])}
d3

{'k1': [0, 21, 42, 63, 84], 'k2': [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]}
{'k3': 495}

# In[ ]:




