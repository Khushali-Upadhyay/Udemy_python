#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Task-1 Import random inside a function with two parameters


# In[10]:


def compute(rad, num):
    
    import random as rd
    
    rd.seed(10)
    
    numbers = range(1, rd.randint(1, rad))
    
    calc = []
    for i in range(len(numbers)):
        
        if numbers[i]  %2 == num and numbers[i] > 10:
            s = numbers[i]
            calc.append(s)
            
        else:
            s = 0
            calc.append(s)
            
        print(sum(calc))
        
        return calc





# In[11]:


compute(20, 0)
56
[0,0,0,0,0,0,0,0,0,0,11,0,13,0,15,0,17,0]
compute(20, 1)
60
[0,0,0,0,0,0,0,0,0,0,0,12,0,14,0,16,0,18]

# In[ ]:


#Task-2 Call a nested function and modify its default parameter


# In[12]:


def lang(program = "Javascript"):
    print ("My favourite language is {}.".format(program))
    
def udemy(program):
    lang(program)
    print("The coolest part about {} is functions".format(program))
udemy("Python")


# In[ ]:

My favourite language is Python.
The coolest part about Python is functions.
#Task-3 Function repeats another function with input


# In[ ]:


define greet(name = "Michael"):
    print ("Hello there, " + name, "!")


# In[ ]:


def repeat(n):
    for i in range(n):
        name = input("Student name: " )
        greet(name)
repeat(3)


# In[ ]:

Student name:Michael
Hello there, Michael!
Student name:Sarah
Hello there, Sarah!
Student name:Callum
Hello there, Callum!

#Task-4 Function with control flow and formatting


# In[ ]:


def survivor(name = "Michael "):
    zomb1 = input("How many zombies are there?")
    zombie = eval(zomb1)
    
    if zombie >= 1 and zombie < 20:
        print("{} is fighting {} zombies!".format(name, zombie))
    elif zombie >= 20 and zombie <100:
        print("{} is shooting {} zombies!".format(name, zombie))
    elif zombie >=100 and zombie < 200: 
        print("{} is running room {} zombies!".format(name, zombie))
    else:
        print("{} is eaten ALIVE by {} zombies !!!!!".format(name, zombie))


# In[ ]:


survivor("Daryl")


# In[ ]:

How many zombies are there?110
Michael is running from 110 zombies

How many zombies are there?9
Michael is fighting 9 zombies

How many zombies are there?220
Daryl is eaten ALIVE by 220 zombies!!!!!


# In[ ]:




