#Task-1 Convert functions into lamda expressions


# In[ ]:


def mul(num1=5, num2=20, num3=100):
    return num1+num2+num3


bowl=["cherries", "orange", "apple", "melon", "figs"]
def salad(fruit):
    if fruit in bowl:
        print(fruits)
    else:
        print("not in bowl")
        
def inside(num):
    if num in list(range(10)):
        return num**2
        else:
            print("outside")


# In[2]:


mul = lambda num1 = 5, num2 = 20, num3=100: num1+num2+num3
mul()

125

# In[3]:


bowl=["cherries", "orange", "apple", "melon", "figs"]
salad = lambda x : "fruit" if x in bowl else "not in bowl"

salad("mango")

'not in bowl'

# In[4]:


inside = lambda num: num**2 if num in range(10) else "outside"
inside(4)

16

# In[ ]:


#Task-2 Handling errors with Lamda and while loop


# In[ ]:


while True:
    try:
        val = int (eval(input("Enter an integer:")))
        g = lamda x: x*3 if x > 10 else "too low"
            ### Control Flow Goes here ###
            g(value)>20
            ##################################
            except :
                continue
                
            finally:


# In[5]:


def error():
    while True:
        try:
            val=int(eval(input("Enter an integer:")))
            g = lambda x: x*3 if x > 10 else "too low"
            
            if g(val) > 20:
                print ("Lamda is ", g(val))
                print("Input value is", val)
                break
                
            else:
                print("No output")
                
        except:
            print("Try again, please")
            continue
            
        finally:
            print("END CODE")
error()

Enter an integer:1
Try again, please
END CODE
Enter an integer:10
Try again, please
END CODE
Enter an integer:12.12345
Lamda is  36
Input value is 12
END CODE

# In[ ]:


#Task-3 Use for loops with lambda


# In[ ]:


g = lamda x: x**2 if x > 5 in range(10) else 0


# In[6]:


g = lambda x: x**2 if x > 5 in range(10) else 0

for i in range(10):
    print(i+100, i + g(3))  #9

00 0                
101 1
102 2
103 3
104 4
105 5
106 6
107 7
108 8
109 9


# In[ ]:


#Task-4 For loop and list comprehension


# In[13]:


critics = ("Mustafa", "Michael", "Callum", "George")
films = ["Akira", "Blade Runner 2049", "Mr. Robot", "The Ten Commandments"]


# In[14]:


opinion = []

for i in range(4):
    fave = critics[i] + "'s favourite film is " + films[i]
    opinion.append(fave)
opinion


["Mustafa's favourite film is Akira",
 "Michael's favourite film is Blade Runner 2049",
 "Callum's favourite film is Mr. Robot",
 "George's favourite film is The Ten Commandments"]


# In[15]:


[critics[i] + "'s favourite film is " + films[i] for i in range(4)]

["Mustafa's favourite film is Akira",
 "Michael's favourite film is Blade Runner 2049",
 "Callum's favourite film is Mr. Robot",
 "George's favourite film is The Ten Commandments"]

# In[ ]:





# In[ ]:




