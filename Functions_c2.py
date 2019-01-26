#!/usr/bin/env python
# coding: utf-8

# In[1]:


def square(arg1, arg2):
    return(arg1 + arg2)
num = square(20, 50)


# In[2]:

num
70

# In[ ]:


def square(arg1=20, arg2=70):
    return(arg1 + arg2)
num = square()


# In[3]:


num

70

# In[8]:


def square(arg1=20, arg2=50):
    """This adds two numbers together"""
    return( arg1 + arg2)
value = square(90, 110)
type(square)

function

# In[9]:


def squared(num):
    return num**2
def cubed(num):
    return num**3
def quad(num):
    return num**4
v = 4
print(squared(v))
print(cubed(v))
print(quad(v))
total = squared(v) + cubed(v) + quad(v)
total

16
64
256

# In[12]:


def greet():
    """Enter the time and print appropriate greeting"""
    time = eval(input("Enter the time:"))
    
    if time >= 6 and time < 12:
        print("Good morning!")
    elif time >= 12 and time < 18:
        print("Afternoon!")
    elif time >= 18 and time < 21:
        print("Good evening!")
    else:
        print("Good night!")
        
greet()    

Enter the time:15
Afternoon!

# In[13]:


def greet():
    """Enter the time and print appropriate greeting"""
    time = eval(input("Enter the time:"))
    
    if time >= 6 and time < 12:
        print("Good morning!")
        return squared(time)
    elif time >= 12 and time < 18:
        print("Afternoon!")
        return cubed(time)
    elif time >= 18 and time < 21:
        print("Good evening!")
        return quad(time)
    else:
        print("Good night!")
        return time
        
greet()    

Enter the time:12
Afternoon!
1728

# In[ ]:





# In[ ]:





# In[ ]:




