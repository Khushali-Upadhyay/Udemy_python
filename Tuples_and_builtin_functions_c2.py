tup1 = 10, 20, 30, 40
tup1

(10, 20, 30, 40)

# In[5]:


mylist = [50, 60, 70]
tup2 = tuple(mylist)
tup2

(50, 60, 70)


# In[6]:


tup3 = tup1 + tup2
tup3

(10, 20, 30, 40, 50, 60, 70)


# In[7]:


tup4 = "cat" , "cat", "cat", "dog", "dog", 10, 10, 10, 10, True
tup4.count("dog")

2


# In[8]:


tup4 = "cat" , "cat", "cat", "dog", "dog", 10, 10, 10, 10, True
tup4.count(10)

4


# In[9]:


tup3

(10, 20, 30, 40, 50, 60, 70)


# In[11]:


tup3.index(40)

3


# In[12]:


tup3[3]

40

# In[13]:


sum(tup1)

100

# In[14]:


sum(tup1*2)

200

# In[15]:


max(tup3)

70

# In[16]:


min(tup3)

10

# In[17]:


tup3
tuple(sorted(tup3))

(10, 20, 30, 40, 50, 60, 70)

# In[18]:


tup1[0] = "dog"

TypeError                                 Traceback (most recent call last)
<ipython-input-18-bb061c34e219> in <module>
----> 1 tup1[0] = "dog"

TypeError: 'tuple' object does not support item assignment






