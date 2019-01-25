#!/usr/bin/env python
# coding: utf-8

# In[1]:


cosmos = []
for i in "universe":
    cosmos.append(i)
cosmos
    
['u', 'n', 'i', 'v', 'e', 'r', 's', 'e']

# In[3]:


[u for u in "universe"]

['u', 'n', 'i', 'v', 'e', 'r', 's', 'e']


# In[5]:


list("universe")

['u', 'n', 'i', 'v', 'e', 'r', 's', 'e']


# In[6]:


norm = []
for n in range(0, 11):
    result = n ** 2
    norm.append(result)
norm

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# In[7]:


comp = [x**2 for x in range(0, 11)]
comp

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# In[10]:


pets = ["cat", "dog", "rabbit", "duck", "mouse", "piglet"]
rad = []
for i in range(len(pets)):
    res = pets[i] + "is hungry!"
    rad.append(res)
rad

['catis hungry!',
 'dogis hungry!',
 'rabbitis hungry!',
 'duckis hungry!',
 'mouseis hungry!',
 'pigletis hungry!']

# In[11]:


[pets[i] + " is hungry!" for i in range(len(pets))]

['catis hungry!',
 'dogis hungry!',
 'rabbitis hungry!',
 'duckis hungry!',
 'mouseis hungry!',
 'pigletis hungry!']


# In[12]:


[numbers**3 for numbers in range(0,11) if numbers >= 3 and numbers % 2 == 1]

[27, 125, 343, 729]

# In[13]:


count = []
for num in range(0, 11):
    if num >= 3 and num % 2 ==1:
        new = num**3
        count.append(new)
count        

[27, 125, 343, 729]

# In[14]:


growth = []
for grow in range(0, 20):
    if grow % 2 == 0 and grow > 2:
        growth.append(grow)
growth

[4, 6, 8, 10, 12, 14, 16, 18]

# In[15]:


[g for g in range(0, 20) if g % 2 == 0 and g > 2]

[4, 6, 8, 10, 12, 14, 16, 18]


# In[ ]:




