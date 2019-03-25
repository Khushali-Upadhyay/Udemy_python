help(print)

Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.


# In[2]:


import random as rd
rd.seed(10)

numbers = rd.sample(range(10, 100), k = 10)
numbers

[83, 14, 64, 71, 11, 36, 69, 72, 45, 93]


# In[3]:


max(numbers)

93


# In[4]:


min(numbers)

11

# In[5]:


sum(numbers)

558

# In[6]:


round(9.12345, 4)

9.1235


# In[7]:


abs(-10)

10

# In[8]:


abs(10)

10

# In[9]:


eval("4.5")

4.5

# In[10]:


eval("9")

9

# In[11]:


pow(4, 2)

16

# In[12]:


new_numbers = sorted(numbers)
new_numbers

[11, 14, 36, 45, 64, 69, 71, 72, 83, 93]

# In[13]:


numbers

[83, 14, 64, 71, 11, 36, 69, 72, 45, 93]

# In[14]:


[pow(x, 2) for x in new_numbers]

[121, 196, 1296, 2025, 4096, 4761, 5041, 5184, 6889, 8649]

# In[16]:


[i > 40 for i in new_numbers]

[False, False, False, True, True, True, True, True, True, True]

# In[18]:


any([i > 40 for i in new_numbers])

True


# In[19]:


all([i > 40 for i in new_numbers])

False

# In[20]:


sum([i > 40 for i in new_numbers])

7

# In[7]:


data = ["10", 8.12345, 100, -30, -200]
data

['10', 8.12345, 100, -30, -200]

# In[9]:


new_data = eval(data[0]) + int(data[1]) + data[2] + abs(data[3]) + abs(data[4])
new_data


348

# In[10]:


data

['10', 8.12345, 100, -30, -200]

# In[18]:


"The top 3 values {0}, {1}, and {2}.My favourite number is {2}".format(*clean_data)

'The top 3 values 200, 100, and 30.My favourite number is 30'

# In[11]:


[int(i) for i in data]

[10, 8, 100, -30, -200]

# In[15]:


clean_data = sorted([abs(k) for k in [int(i) for i in data]])
clean_data

[8, 10, 30, 100, 200]

# In[16]:


clean_data = sorted([abs(k) for k in [int(i) for i in data]])[2:]
clean_data

[30, 100, 200]

# In[17]:


clean_data = sorted([abs(k) for k in [int(i) for i in data]])[2:][3::-1]
clean_data

[200, 100, 30]

# In[ ]:





# In[ ]:





# In[ ]:




