#Task-1:Add all dictionary values


# In[1]:


toys = {"robot":"$40.0","car":"$25","ironman":"$12"}
toys

{'robot': '$40.0', 'car': '$25', 'ironman': '$12'}

# In[2]:


toys.values()

dict_values(['$40.0', '$25', '$12'])


# In[29]:


num = int(eval(list(toys.values())[0][1:]) + eval(list(toys.values())[1][1:]) + eval(list(toys.values())[2][1:]))
num

77.0


# In[ ]:


# Task-2 Use comparison operators in a list


# In[ ]:


questions = [10 4, 50 50, 90 10, "c" ("a", "b","c"), 100 100]


# In[34]:


questions = [10 != 4,50 == 50, 90 == 10, "c" in ("a", "b","c"), 100 != 100]
questions

[True, True, False, True, False]


# In[ ]:


# Len key values with comparison operators


# In[45]:


films = {"k1":"Blade runner 20149","k2":"matrix","k3":"ninja scroll"}
films

{'k1': 'Blade runner 20149', 'k2': 'matrix', 'k3': 'ninja scroll'}


# In[43]:


len(films["k1"]) > len(films["k2"]) < len(films["k3"])

True


# In[ ]:


#Update Dictionary


# In[40]:


life_stages = {0:"embryo", 1:"fetus", 2:"baby", 3:"infant", 4:"teen"}
life_stages

{0: 'embryo', 1: 'fetus', 2: 'baby', 3: 'infant', 4: 'teen'}

# In[53]:


midlife = {5:"adult", 6:"big kid!"}
midlife

{5: 'adult', 6: 'big kid!'}


# In[56]:


life_stages.update(midlife)
life_stages


{0: 'embryo',
 1: 'fetus',
 2: 'baby',
 3: 'infant',
 4: 'teen',
 5: 'adult',
 6: 'big kid!'}


# In[ ]:


# Add all values from list


# In[57]:


nest1 = [(1, 2, 3), {"k1": [8, 1, 300, 2, 77], "k2":[10, 20, 30]}, ["a", "500", "c"]]
nest1


[(1, 2, 3), {'k1': [8, 1, 300, 2, 77], 'k2': [10, 20, 30]}, ['a', '500', 'c']]

# In[104]:


float(nest1[0][2] + sorted(nest1[1]["k1"])[-1] + sorted(nest1[1]["k2"])[-1] + eval(nest1[2][1]))

833.0

# In[ ]:


#Add all list values in the string


# In[114]:


prices = ["a", "b", "9", "c", "d", "FOUR", "e", "f", "2.5"]
cash = prices[2::3]
p = eval(cash[0])
c = len(cash[1])
d = eval(cash[2])


# In[108]:


sentence = """"The bill for the {}#!/,?? {}#!/ ?? and drink came to {}??"""


# In[115]:


sentence.format("pizza", "chips", "$" + str(p+c+d)).replace("??", "").replace("#!/", "")


'"The bill for the pizza, chips  and drink came to $15.5'






