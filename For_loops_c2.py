#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(0, 11, 2):
    print(i)

0
2
4
6
8
10

# In[2]:


for greeting in range(4):
    print("Hello World!")

Hello World!
Hello World!
Hello World!
Hello World!


# In[3]:


cats = {"tiger", "lion", "jaguar", "leopard"}
for cat in cats:
    print(cat)

lion
leopard
jaguar
tiger

# In[4]:


for num in range(4):
    print(num, num + 30)

0 30
1 31
2 32
3 33

# In[5]:


nest1 = [[10, 20, 30], [3.5, 4.5, 5.5], ["sword", "hammer", "sheild"]]
for i in range(3):
    print(nest1[i])

[10, 20, 30]
[3.5, 4.5, 5.5]
['sword', 'hammer', 'sheild']


# In[7]:


for i in range(3):
    res = nest1[0][i] + nest1[1][i]
    
    print(nest1[2][i].capitalize() + ": Power level =", res)

Sword: Power level = 13.5
Hammer: Power level = 24.5
Sheild: Power level = 35.5


# In[11]:


weapons = []
for i in range(3):
    s = nest1[2][i].capitalize() + ": Power level =" + str(nest1[0][i] + nest1[1][i])
    weapons.append(s)
weapons

['Sword: Power level =13.5',
 'Hammer: Power level =24.5',
 'Sheild: Power level =35.5']

# In[12]:


for i in range(1, 8):
    print("{} + {} = {}".format(i, i, (i+i)))


1 + 1 = 2
2 + 2 = 4
3 + 3 = 6
4 + 4 = 8
5 + 5 = 10
6 + 6 = 12
7 + 7 = 14

# In[13]:


tup1 = ((10, 20), ("a", "b"), (100, 200))
for t in tup1:
    print(t)

(10, 20)
('a', 'b')
(100, 200)


# In[15]:


tup1 = ((10, 20), ("a", "b"), (100, 200))
for i in range(2):
    for x, y in tup1:
        print(x, y)

10 20
a b
100 200
10 20
a b
100 200


# In[16]:


cakes = ["chocolates", "lemon", "carrot", "vanilla"]
d1 = {"k1": tuple(cakes), "k2": [10, 20, 30, 40]}
d1["k1"]

('chocolates', 'lemon', 'carrot', 'vanilla')


# In[17]:


for d in d1["k2"]:
    print(d)

10
20
30
40

# In[18]:


for x in d1:
    for i in range(4):
        print(x, ":", d1[x][i])

k1 : chocolates
k1 : lemon
k1 : carrot
k1 : vanilla
k2 : 10
k2 : 20
k2 : 30
k2 : 40

# In[22]:


cats 
endangered = ["series", "critical",
              "very critical", "stable"]

for c in range(4):
    print(cats[c].capitalize(), "\n Level: \n", endangered[c].upper())


# In[ ]:





# In[ ]:





# In[ ]:




