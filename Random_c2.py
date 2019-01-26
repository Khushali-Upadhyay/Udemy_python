#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random as rd


# In[3]:


dir(random)
['BPF',
 'LOG4',
 'NV_MAGICCONST',
 'RECIP_BPF',
 'Random',
 'SG_MAGICCONST',
 'SystemRandom',
 'TWOPI',
 '_BuiltinMethodType',
 '_MethodType',
 '_Sequence',
 '_Set',
 '__all__',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 '_acos',
 '_bisect',
 '_ceil',
 '_cos',
 '_e',
 '_exp',
 '_inst',
 '_itertools',
 '_log',
 '_os',
 '_pi',
 '_random',
 '_sha512',
 '_sin',
 '_sqrt',
 '_test',
 '_test_generator',
 '_urandom',
 '_warn',
 'betavariate',
 'choice',
 'choices',
 'expovariate',
 'gammavariate',
 'gauss',
 'getrandbits',
 'getstate',
 'lognormvariate',
 'normalvariate',
 'paretovariate',
 'randint',
 'random',
 'randrange',
 'sample',
 'seed',
 'setstate',
 'shuffle',
 'triangular',
 'uniform',
 'vonmisesvariate',
 'weibullvariate']


# In[4]:


len(dir(random))

62

# In[16]:


import random as rd
from random import *     #Call function directly


# In[12]:


rd.random()
rd.randint(10, 20)

20

# In[14]:


rd.randrange(10, 100, 10)

50

# In[17]:


random()
randint(10, 20)

12

# In[19]:


[rd.randint(50, 100)]*4

[91, 91, 91, 91]


# In[21]:


rd.uniform(2, 3)

2.706192499621014


# In[34]:


animals = "\N{cat}", "\N{dog}", "\N{snake}", "\N{horse}"
animals


# In[35]:


type(animals)

tuple


# In[38]:


animals = ["\N{cat}", "\N{dog}", "\N{snake}", "\N{horse}"]
rd.shuffle(animals)
animals


# In[44]:


heroes = ["Batman", "Spiderman", "Ironman", "Captain America"]
villains = ["Joker", "Venom", "Thanos", "Red Skull"]
numbers = list(range(len(heroes)))
numbers

rd.shuffle(heroes); rd.shuffle(villains)
for i in numbers:
    print(heroes[i], "VS", villains[i])

Spiderman VS Red Skull
Captain America VS Venom
Batman VS Joker
Ironman VS Thanos

# In[46]:


menu = ["noodles", "cashew with tofu", "coconut rice"]
rd.choice(menu)

'coconut rice'

# In[51]:


probabilities = [0.9, 0.01, 0.01, 0.08]
students = ["Gracie", "Callum", "Blaise", "Tommy"]
rd.choices(students, probabilities)

['Blaise']

# In[53]:


rd.sample(range(10, 40), k=3)

[33, 10, 37]

# In[ ]:




