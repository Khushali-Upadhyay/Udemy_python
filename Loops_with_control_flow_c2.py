#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(10):
    if i == 4:
        print("MORNING!")
    elif i == 7:
        print("NIGHT!")
    else:
        print(i)

0
1
2
3
MORNING!
5
6
NIGHT!
8
9


# In[2]:


x = 0
while x < 10:
    if x == 6:
        print("Hello there!")
    elif x > 8:
        print("Good morning")
    else:
        print("cool")
    x += 1


cool
cool
cool
cool
cool
cool
Hello there!
cool
cool
Good morning



# In[4]:


for s in range(10):
    if s == 6:
        print("Hello there!")
    elif s > 8:
        print("Good morning")
    else:
        print("cool")
    s += 1


cool
cool
cool
cool
cool
cool
Hello there!
cool
cool
Good morning


# In[7]:


num = [10, 5, 20, 3, 100, 4, 7]
rad = [4, 1, 40, 3, 120, 5, 7 ]


# In[8]:


x = 0
while x < len(num):
    if num[x] == rad[x]:
        print("Equal")
    elif num[x] > rad[x]:
        print("Greater")
    else:
        print("less")
    x += 1

Greater
Greater
less
Equal
less
less
Equal


# In[9]:


for x in range(len(num)):
    if num[x] == rad[x]:
        print("Equal")
    elif num[x] > rad[x]:
        print("Greater")
    else:
        print("less")
    x += 1

Greater
Greater
less
Equal
less
less
Equal






