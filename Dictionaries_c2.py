d1 = {}
d1["A"] = 10
d1["B"] = 20
d1["C"] = 50
d1

{'A': 10, 'B': 20, 'C': 50}

# In[4]:


toys = {"robot" :"$25.99", "car" : "45.95"}
toys

{'robot': '$25.99', 'car': '45.95'}


# In[5]:


toys = {"robot" :"$25.99", "car" : "45.95"}
d1.update(toys)
d1

{'A': 10, 'B': 20, 'C': 50, 'robot': '$25.99', 'car': '45.95'}


# In[6]:


d1

{'A': 10, 'B': 20, 'C': 50, 'robot': '$25.99', 'car': '45.95'}


# In[9]:


d1["A"] = 120
d1

{'A': 120, 'B': 20, 'C': 50, 'robot': '$25.99', 'car': '45.95'}


# In[11]:


mylist = [10, 20]
mylist[0] = 120
mylist

[120, 20]


# In[12]:


toys.clear()
toys

{}


# In[13]:


mylist.clear()
mylist

[]


# In[14]:


mylist = [10, 20]
mylist.append(300)
mylist

[10, 20, 300]


# In[15]:


d1

{'A': 120, 'B': 20, 'C': 50, 'robot': '$25.99', 'car': '45.95'}

# In[16]:


d1.pop("A")
d1

{'B': 20, 'C': 50, 'robot': '$25.99', 'car': '45.95'}

# In[17]:


d1

dict_values([20, 50, '$25.99', '45.95'])

# In[18]:


d1.values()

dict_values([20, 50, '$25.99', '45.95'])


# In[19]:


#Convert into list or tuple for indexing
list(d1.values())[2:4]

['$25.99', '45.95']


# In[20]:


d1.keys()

dict_keys(['B', 'C', 'robot', 'car'])


# In[21]:


#Convert into list or tuple for indexing
tuple(d1.keys())[2:4]

('robot', 'car')


# In[22]:


d1.items()

dict_items([('B', 20), ('C', 50), ('robot', '$25.99'), ('car', '45.95')])



# In[23]:


list(d1.items())

[('B', 20), ('C', 50), ('robot', '$25.99'), ('car', '45.95')]


# In[24]:


list(d1.items())[0]

('B', 20)


# In[25]:


dict(d1.items())

{'B': 20, 'C': 50, 'robot': '$25.99', 'car': '45.95'}


# In[26]:


menu = [("chips", 2.4), ("soup", 1.4)]
dict(menu)

{'chips': 2.4, 'soup': 1.4}


# In[28]:


maze = {"k1":d1,
       "k2":[10, 20, 30],
       "k3":("tuple",[1, 2,{"k4":["a","b", "catch me!"]}])}
maze


{'k1': {'B': 20, 'C': 50, 'robot': '$25.99', 'car': '45.95'},
 'k2': [10, 20, 30],
 'k3': ('tuple', [1, 2, {'k4': ['a', 'b', 'catch me!']}])}

# In[30]:


maze["k3"][1][2]["k4"][2]

catch me!'

# In[32]:


num = "200"
eval(num)


# In[ ]:




