#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = "George" ; grade = "A++"
"The student's name is {} and the grade is {}".format(name,grade)

"The student's name is George and the grade is A++"
# In[4]:


animals = ["lions" , "elephants", "zebras"]
safari = "I saw {}, {} and {}!"




# In[5]:


safari.format(animals[0].upper, animals[1].capitalize, animals[2].upper)
'I saw LIONS, Zebras and ELEPHANTS!'


# In[6]:


safari.format(*animals)
'I saw lions, zebras and elephants!'


# In[9]:


num = "200"
eval(num) + 10

numbers = [10, 20, 30]
eval("{} + {} + {}".format(*numbers))

60

# In[10]:


numbers = [10, 20, 30]
eval("{0} + {0} + {0}".format(*numbers))

30

# In[11]:


"%d * %d = %d" % (10, 20, (10 * 20))

'10 * 20 = 200'

# In[15]:


"%d * %d = %.2f" % (5, 3, (5/3))

'5 * 3 = 1.67'

# In[16]:


word = "awesome"
"The length of this word {} is {}".format(word,len(word))

'The length of this word awesome is 7'


# In[17]:


"days left are {num: .10f}".format(num = 300/9)

'days left are 33.3333333333'


# In[18]:


num = 300/9
f"days left are {num: .10f}"

'days left are 33.3333333333'


# In[20]:


p1 = "Python" ; p2 = "older"
f"""This is a docstring that uses {p1} 3.6 and caqnt be used for {p2} versions of {p1} """.replace("\n", "").upper()


'THIS IS A DOCSTRING THAT USES PYTHON 3.6 AND CAQNT BE USED FOR OLDER VERSIONS OF PYTHON '
# In[ ]:




