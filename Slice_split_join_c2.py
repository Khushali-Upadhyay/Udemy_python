robot = "technologically"
consoles = "ps4 is cooler than xbox!"
code = "p1y2t3h4o5n6i7c8"
words = "I saw a cat jump over the moon and into the clouds."
new_words = "I saw a cow fly over the gates and into the forest"
paid = "I received a total of $5000. "


# In[3]:


len(robot)

15

# In[4]:


robot

'technologically'


# In[5]:


robot[0:6]
'techno'


# In[6]:


robot[6:]

'logically'

# In[8]:


robot[10:14]

'call'


# In[9]:


consoles.endswith("!")

True


# In[10]:


len(consoles)

24

# In[11]:


consoles[23]

!


# In[12]:


consoles.find("!")

23


# In[13]:


consoles

'ps4 is cooler than xbox'


# In[14]:


consoles[7:13]

'cooler'


# In[15]:


consoles[-1]

'!'

# In[16]:


consoles[23]

'!'

# In[17]:


consoles[-17:-11]

'cooler'

# In[18]:


code

'p1y2t3h405n6i7c8'


# In[19]:


code.replace("l","").replace("2","")

'pyt3h4o5n6i7c8'


# In[20]:


code[0:1] + code[2:3] + code[4:5]

'pyt'


# In[21]:


code[0::2].upper()

'PYTHONIC'


# In[22]:


code[1::2]

'123456'


# In[23]:


words

'I saw a cat jump over the moon and into the clouds.'


# In[24]:


var = words.split()
var

['I',
 'saw',
 'a',
 'cat',
 'jump',
 'over',
 'the',
 'moon',
 'and',
 'into',
 'the',
 'clouds']


# In[25]:


len(var)
var[3:]

['cat','jump','over','the','moon','and','into','the','clouds']


# In[26]:


len(var)
var[3:8]

['cat','jump','over','the','moon']

# In[ ]:


len(var)
var[3:8:2]

['cat','over','moon']


# In[27]:


new_words

'I saw a cow fly over the gates and into the forest'


# In[28]:


s1  = slice(3,12,2)
new_words.split()[s1]

['cow','over','moon','into','clouds']     #Doubt


# In[29]:


var[s1]

['cat','over','moon','into','clouds']     #Doubt

# In[30]:


"dog" not in var

True


# In[31]:


" ".join(var)

'I saw a cat jump over the moon and into the clouds'


# In[32]:


pay



# In[33]:


pay.split("$")[1]

'5000'

# In[ ]:




