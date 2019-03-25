# In[2]:


a = 10; b = 25; c = 100; d = ("cat", "dog", "bird")


# In[3]:


if a == 10 and b < 40:
    print("This is true!")

This is true!


# In[4]:


if a == 10:
    if b < 40:
        print("This is true!")

This is true!

# In[5]:


if a == 10 and b < 40:
    print("This is true!")
else:
    print("This is true!")

This is true!


# In[6]:


if a == 10:
    print("a is true")
    
    if b < 40:
        print("b is true")
    else:
        print("b is false")
        
else:
    print("b is false")


a is true
b is true


# In[7]:


if a == 10:
    print("a is true")
    
    if b < 4:
        print("b is true")
    else:
        print("b is false")
        
else:
    print("b is false")


a is true
b is false


# In[8]:


if a == 100:
    print("a is true")
    
    if b < 4:
        print("b is true")
    else:
        print("b is false")
        
else:
    print("b is false")


b is false


# In[9]:


if a == 10:
    print("a is true")
    
    if b < 4:
        print("b is true")
        
        if c > 9:
            print("c is true")
        else:
            print("c is false")
        
    else:
        print("b is false")
        
else:
    print("b is false")


a is true
b is false


# In[10]:


if a == 10:
    print("a is true")
    
    if b < 40:
        print("b is true")
        
        if c > 9:
            print("c is true")
        else:
            print("c is false")
        
    else:
        print("b is false")
        
else:
    print("b is false")


a is true
b is true
c is true

# In[11]:


if a == 10:
    print("a is true")
    
    if b < 40:
        print("b is true")
        
        if c > 9:
            print("c is true")
            
            if "cat" in d:
                print("d is true")
            else:
                print("d is false")
        else:
            print("c is false")
        
    else:
        print("b is false")
        
else:
    print("b is false")


a is true
b is true
c is true
d is true


# In[12]:


num = eval(input("Enter the number:"))
num

Enter the number:100
100


# In[14]:


num = eval(input("Enter the number:"))

if num >=3:
    print("Keep looking")
    
elif d[num] == "cat":
    print("Found a {}".format(d[num]))
elif d[num] == "cat":
    print("Found a {}".format(d[num]))
else:
    print("Found a bird")

Enter the number:0
Found a cat


# In[15]:


d

('cat', 'dog', 'bird')


# In[18]:


total = [list(range(11)), list(range(11, 21)), list(range(21, 31))]
total

[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
 [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
 [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]


# In[17]:


total[0]

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[21]:


v = eval(input("Enter the number"))

if v in total[0]:
    print(v, "in list one")
elif v in total[1]:
    print(v, "in list two")
elif v in total[2]:
    print(v, "in list three")
else:
    print(v, "not in any list")


Enter the number2
2 in list one








