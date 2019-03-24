

# In[ ]:


#Task-1 Compare two txt files


# In[6]:


d = open("rain.txt", "w")
d.write("Hi")
d.write("\nFood is hot"*2)
d.write("\nSunny Day"*4)
d.close()

e = open("cloud.txt", "w")
e.write("Hi")
e.write("\nFood is cold"*2)
e.write("\nSunny Day"*4)
e.close()


# In[7]:


a = open("rain.txt", "r")
b = open("cloud.txt", "r")
day = a.readlines()
night = b.readlines()
for i in range(6):
    if day[i] == night[i]:
        print(True)
    else:
        print(False)
a.close()
b.close()

True
False
False
True
True
True

# In[10]:


a, b = open("rain.txt", "r"), open("cloud.txt", "r")
day, night = a.readlines(), b.readlines()
for i in [True if day[i] == night[i] else False for i in range(6)]:
    print(i)
a.close(); b.close()

True
False
False
True
True
True


# In[ ]:


#Create three txt files with one input each


# In[14]:


files = ["morning", "evening", "night"]
for i in range(len(files)):
    d = open(files[i] +".txt", "w")
    d.write("game")
    d.close()
    text = input("add text:")
    
    d = open(files[i] +".txt", "a")
    d.write("\n" + text)
    d.close()
    
#Creates 3 different files and writes the following text in each


# In[ ]:

add text:win
add text:lose
add text:draw


#Task-3 Filter out words based on length


# In[15]:


w = open("count.txt", "w")
w.write("""computer\n
python\n
udemy\n
intelligence\n
universal\n
jupyter\n
java\n
javascript""")
w.close()

with open("count.txt", "r+") as comp:
    g = "".join(comp.readlines())
g2 = g.replace("\n\n", " ").split()

[i for i in g2 if len(i) >= 5 and len(i) <= 7]


# In[ ]:

['python', 'udemy', 'jupyter']






