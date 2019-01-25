#!/usr/bin/env python
# coding: utf-8

# In[4]:


for num in range(40):
    if num > 10 and num <= 20:
        if num == 16:
            pass               #Ignores the if statement
        print(num)

11
12
13
14
15
16
17
18
19
20



# In[5]:


for num in range(40):
    if num > 10 and num <= 20:
        if num == 16:
            break
        print(num)

11
12
13
14
15


# In[6]:


for num in range(40):
    if num > 10 and num <= 20:
        if num == 16:
            continue
        print(num)

11
12
13
14
15
17
18
19
20


# In[9]:


for word in "ComputAtion":
    if word == "A":
        pass
        
    print(word) 


C
o
m
p
u
t
A
t
i
o
n

# In[10]:


for word in "ComputAtion":
    if word == "A":
        break
        
    print(word) 


C
o
m
p
u
t



# In[11]:


for word in "ComputAtion":
    if word == "A":
        continue
        
    print(word) 


C
o
m
p
u
t
t
i
o
n

# In[12]:


for word in "ComputAtion":
    if word == "A" or word == "p":
        continue
        
    print(word) 

C
o
m
u
t
t
i
o
n


# In[13]:


for word in "ComputAtion":
    if word == "A" or word == "p":
        break
        
    print(word) 

C
o
m


# In[14]:


for word in "ComputAtion":
    if word == "A" and word == "p":
        break
        
    print(word) 

C
o
m
p
u
t
A
t
i
o
n

# In[15]:


for word in "ComputAtion":
    if word == "A" and word == "p":
        continue
        
    print(word) 

C
o
m
p
u
t
A
t
i
o
n


# In[ ]:




