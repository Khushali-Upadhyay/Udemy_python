#!/usr/bin/env python
# coding: utf-8

# In[1]:


list(range(11))

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# In[2]:


list(range(5, 11))
[5, 6, 7, 8, 9, 10]

# In[3]:


list(range(0, 20, 2))

[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# In[4]:


list(range(-50, 60, 10))

[-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50]


# In[5]:


nest = [[1, 2, 3],[4, 5, 6]]
nest[0]

[1, 2, 3]


# In[6]:


nest = [[1, 2, 3],[4, 5, 6]]
nest[0]*2

[1, 2, 3, 1, 2, 3]

# In[9]:


nest = [[1, 2, 3],[4, 5, 6]]
new = [list(range(5)), list(range(5,10))]
nest + new

[[1, 2, 3], [4, 5, 6], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]

# In[ ]:


num = [32, 2, 45, 22]
num



# In[13]:


num = [32, 2, 45, 22]
num.append(100)
num

[32, 2, 45, 22, 100]

# In[14]:


num.clear()
num

[]


# In[16]:


num.append([32, 2, 45, 22, 100])


# In[21]:


num = num[0]


# In[22]:


num

32


# In[24]:


num = [32, 2, 45, 22]
num.sort()
num

[2, 22, 32, 45]
# In[25]:


num = [32, 2, 45, 22]
num.reverse()
num

[22, 45, 2, 32]
# In[26]:


num = [32, 2, 45, 22]
num.insert(2,200)
num

[32, 2, 200, 45, 22]


# In[27]:


num = [32, 2, 45, 22]
num.pop()
num

[32, 2, 45]


# In[28]:


items = ["car", "ball", "robot"]
items

['car', 'ball', 'robot']


# In[29]:


items = ["car", "ball", "robot"]
items[0] = "ps4"
items

['ps4', 'ball', 'robot']


# In[30]:


items.append(num)
items

['ps4', 'ball', 'robot', [32, 2, 45]]

# In[31]:


items[3]

[32, 2, 45]
# In[32]:


items[3].insert(3,["Hey!"])
items

['ps4', 'ball', 'robot', [32, 2, 45, ['Hey!']]]

# In[33]:


items[3]

[32, 2, 45, ['Hey!']]

# In[34]:


items[3][3]

['Hey!']


# In[35]:


items[3][3][0]

'Hey!'

# In[36]:


type(items[3][3][0])

str

# In[ ]:




