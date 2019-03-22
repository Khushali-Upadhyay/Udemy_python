#!/usr/bin/env python
# coding: utf-8

# In[2]:


desk = "C:/Users/khushali/Desktop/"
f = open(desk +"first.txt", "w")
print(f)
f.close()

<_io.TextIOWrapper name='C:/Users/khushali/Desktop/first.txt' mode='w' encoding='cp1252'>

# In[10]:


desk = "C:/Users/khushali/Desktop/"
f = open(desk +"first.txt", "w")
f.write("This is my first file!")
f.write("\nHello World")
f.close()             
#Will create file first.txt and write the above 2 lines


# In[11]:


f1 = open(desk +"first.txt", "a")
f1.write("\nGood Night!")
f1.close()
#appends f1 with f


# In[12]:


with open(desk + "first.txt", "a") as g:
    g.write("\nCool")
#appends g with f and deletes to file without using the close() method


# In[14]:


f2 = open(desk +"first.txt", "r")
print(f2.read())
f2.close()

This is my first file!
Hello World
Good Night!
Cool

# In[16]:


gear = ["Blade Wolf", "Raiden"]
path = "C:/Users/khushali/Desktop/FILE_{}/second.txt"
for i in range(len(gear)):
    with open(path.format(i), "w") as f3:
        f3.write(gear[0])
        f3.write("\n"+gear[1])
        
        f3.write("\n{} is cooler than {}".format(gear[0], gear[1]))
#creates the files named file_0 and file_1 and creates second.txt in it and writes the data in it


# In[20]:


simpsons = [["Bart in detention", "Lisa at MIT"],
           ["Doughnut...Mmm", "Homer: 'Nom, nom, nom!'"]]
transformers = [["HotRod opens matrix", "Optimus returns!"],
                ["Unicron explodes", "Megatron jumps"]]

def File(text):
    
    path = "C:/Users/khushali/Desktop/"
    
    for i in range(len(text)):
        with open(path +"cartoon_{}.txt".format(i), "w") as f:
            f.write(text[i][0])
            f.write("\n"+text[i][1])
File(simpsons)
#creates cartoon_0 and cartoon_1 and writes data into it


# In[21]:


dc = open("skynet.txt", "w")
dc.write("""Terminator is \n
hunting John connor \n 
and Sarah is protecting him""")
dc.close()
#writes data in skynet.txt

# In[22]:


d = open("skynet.txt", "r+")
d.write("\n hasta la vista baby")
end = d.readlines()
d.close()
#Will be able to write and read


# In[ ]:





# In[26]:





# In[ ]:




