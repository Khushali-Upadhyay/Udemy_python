#Task-1 Convert for loop into a while loop


# In[1]:


numbers=list(range(0,110,10))
numbers=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first = []
for num in numbers:
    s = num * 2.5
    if s % 2 == 0:
        
        first.append(int(s))
first
[0, 50, 100, 150, 200, 250]

# In[2]:


second=[]
x = 0
while x < len(numbers):
    t = numbers[x] * 2.5
    if t % 2 ==0:
        second.append(int(t))
    x += 1
second    

[0, 50, 100, 150, 200, 250]

# In[ ]:


#Task-2 Use len with control flow  in a for loop


# In[4]:


rep = ["Joe", "Mike", "Joi", "Luv", "Deckard", "Wallace", "Rachel"]


# In[5]:


for i in rep:
    if len(i) == 3 or len(i) == 6:
        print(i, "is a replicant")
    else:
        print(i, "is not a replicant")

Joe is a replicant
Mike is not a replicant
Joi is a replicant
Luv is a replicant
Deckard is not a replicant
Wallace is not a replicant
Rachel is a replicant    



# In[ ]:


#Task-3 for loop with nested while loop


# In[ ]:


#Add code here
for r in range(2):
    #Add code here
    #Add code here
        #Add code VV
        k % 2 == 0:
            print("Question")
        #Add code VV
        k > 3 and k < 7:
            print("CELL")
            
        #Add code VV
        k == 3:
            print("INTERLINKED")
        #Add code here
            print("CELL WITHIN CELLS")
        #Add code here!!!
#Add code here


# In[6]:


print("Human")
for r in range(2):
    k = 0
    while k < 8:
        if k % 2 == 0:
            print("Question")
        elif k > 3 and k < 7:
            print("CELL")
        elif k == 3:
            print("INTERLINKED")
        else:
            print("CELL WITHIN CELLS")
        k += 1
print("Time to finish")


Human
Question
CELL WITHIN CELLS
Question
INTERLINKED
Question
CELL
Question
CELL WITHIN CELLS
Question
CELL WITHIN CELLS
Question
INTERLINKED
Question
CELL
Question
CELL WITHIN CELLS
Time to finish

# In[ ]:


#Task-4 Nested for loop in a while loop


# In[7]:


y = 0 ; x = 0
print("START")
while y < 8:
    for x in range(4, 9):
        print("Y =", y)
        print("_________")
        print("X is equal to", x)
        print("_________")
        y += 2; x += 1
print("END")        

START
Y = 0
_________
X is equal to 4
_________
Y = 2
_________
X is equal to 5
_________
Y = 4
_________
X is equal to 6
_________
Y = 6
_________
X is equal to 7
_________
Y = 8
_________
X is equal to 8
_________
END


# In[ ]:


#Task-5 For loop to fix student names


# In[9]:


students = ["nAtalie", "M", "Fa ye", " Callum", "Tara"]

# In[10]:


names = []
for i in students:
    if len(i) > 1:
        s = i.upper().replace(" ", "")
        names.append(s)
tuple(names)        

('NATALIE', 'FAYE', 'CALLUM', 'TARA')

# In[ ]:


#Task-6 For loop with added values from dictionary


# In[12]:


d1 = {"k1": [20, 30, 40], "k2": [1000, 2000, 3000]}


# In[13]:


for i in range(3):
    print("Total =", d1["k1"][i] + d1["k2"][i])
print("End loop")


# In[ ]:

Total = 1020
Total = 2030
Total = 3040
End loop


